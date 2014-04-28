(function (jQuery) {
    
    Backbone._sync = Backbone.sync;
    Backbone.sync = function( method, model, options ) {
        if (method === "delete" || method === "update") {
            return;
        }
       
        return Backbone._sync(method, model, options);
    };
    
    Institution = Backbone.Model.extend({
        urlRoot: '/_main/api/v1/institution/',
        toJSON: function() {
            return this.get('resource_uri');
        },
        toTemplate: function() {
            return _(this.attributes).clone();
        }        
    });    

    Educator = Backbone.Model.extend({
        urlRoot: '/_main/api/v1/educator/',
        toJSON: function() {
            return this.get('resource_uri');
        },
        toTemplate: function() {
            return _(this.attributes).clone();
        },
        parse: function(response) {
            if (response) {
                response.institution = new Institution(response.institution);
            }
            return response;
        }
    });

    EducatorList = Backbone.Collection.extend({
        model: Educator,
        urlRoot: '/_main/api/v1/educator/',
        queryParams: '',
        initialize: function (lst) {
            if (lst !== undefined && lst instanceof Array) {
                for (var i = 0; i < lst.length; i++) {
                    var x = new Educator(lst[i]);
                    this.add(x);
                }
            }
        },
        parse: function(response) {
            return response.objects || response;

        },        
        getByDataId: function(id) {
            var internalId = this.urlRoot + id + '/';
            return this.get(internalId);
        },
        removeByDataId: function(id) {
            var internalId = this.urlRoot + id + '/';
            this.remove(internalId);
        },
        toTemplate: function() {
            var a = [];
            this.forEach(function (item) {
                a.push(item.toTemplate());
            });
            return a;
        },
        url: function() {
            return this.urlRoot + '?' + this.queryParams;
        }
    });
    
    window.EducatorPinView = Backbone.View.extend({
        initialize: function(options) {
            _.bindAll(this,
                      "render",
                      "unrender");
            
            this.parentView = options.parentView;
            this.model.bind("destroy", this.unrender);
            this.render();            
        },
        render: function () {
            var self = this; 
            var institution = this.model.get('institution');

            this.latlng = new google.maps.LatLng(institution.get('latitude'),
                                                 institution.get('longitude'));
            
            for (i=0; i < this.parentView.mapMarkers.length; i++) {
                var pos = this.parentView.mapMarkers[i].getPosition();

                //if a marker already exists in the same position as this marker
                if (this.latlng.equals(pos)) {
                    //update the position of the coincident marker by applying a small multipler to its coordinates
                    var newLat = this.latlng.lat() + (Math.random() - 0.5) / 500;
                    var newLng = this.latlng.lng() + (Math.random() - 0.5) / 500;
                    this.latlng = new google.maps.LatLng(newLat, newLng);
                }
            }
            
            var icon_url = self.model.get('video').length < 1 ?
                'http://teachdentistry.org/site_media/img/icon-pointer-indigo.png' :
                    'http://teachdentistry.org/site_media/img/icon-pointer-red.png';
                
            this.marker = new google.maps.Marker({
                position: this.latlng, 
                title: this.model.get('name'),
                map: this.parentView.mapInstance,
                icon: icon_url
             });
            
            google.maps.event.addListener(this.marker, 'click', function() {
                self.parentView.trigger("markerClicked", self.model, self.marker);
            });
        },
        unrender: function () {
            this.marker.setMap(null);
        }
    });
    
    window.EducatorMapView = Backbone.View.extend({
        events: {
            'click .search_criteria': 'onClickCriteria',
            'click ul.selected_criteria li a': 'onRemoveCriteria'
        },
        initialize: function(options) {
            _.bindAll(this,
                      "render",
                      "renderPopup",
                      "onAddEducator",
                      "onRemoveEducator",
                      "onResetEducators",
                      "onResize",
                      "getVisibleViewport",
                      "toggleAccordion",
                      "onClickCriteria",
                      "onRemoveCriteria");
            
            this.educatorTemplate =
                _.template(jQuery("#educator-template").html());
            this.breadcrumbTemplate =
                _.template(jQuery("#breadcrumbs-template").html());

            this.educators = new EducatorList();
            this.educators.on("add", this.onAddEducator);
            this.educators.on("remove", this.onRemoveEducator);
            this.educators.on("reset", this.onResetEducators);
            
            jQuery(window).on('resize', this.onResize);
            
            jQuery('.collapse').on('hide', this.toggleAccordion);
            jQuery('.collapse').on('show', this.toggleAccordion);
            
            var mapOptions = {
                center: new google.maps.LatLng(39.8282, -98.5795),
                zoom: 4,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            
            var mapCanvas = document.getElementById("map-canvas");
            this.mapInstance = new google.maps.Map(mapCanvas, mapOptions);            
            this.mapMarkers = [];
            
            this.on("markerClicked", this.renderPopup);
            
            jQuery(window).trigger("resize");
            this.educators.fetch();
        },
        getVisibleViewport: function() {
            var viewportwidth;
            var viewportheight;
            
            // the more standards compliant browsers
            // (mozilla/netscape/opera/IE7) use window.innerWidth
            // and window.innerHeight
            if (typeof window.innerWidth != 'undefined') {
                 viewportwidth = window.innerWidth;
                 viewportheight = window.innerHeight;
            } else if (typeof document.documentElement !== 'undefined' &&
                 typeof document.documentElement.clientWidth !=
                'undefined' && document.documentElement.clientWidth !== 0) {
                // IE6 in standards compliant mode (i.e. with a valid 
                // doctype as the first line in the document)
                viewportwidth = document.documentElement.clientWidth;
                viewportheight = document.documentElement.clientHeight;
            } else {
                // older versions of IE
                viewportwidth = document.getElementsByTagName('body')[0].clientWidth;
                viewportheight = document.getElementsByTagName('body')[0].clientHeight;
            }
            
            return { height: viewportheight -
                        (30 + document.getElementById("site-header").clientHeight +
                         document.getElementById("primarynav").clientHeight + 
                         document.getElementById("section-thumbnail").clientHeight),
                     width: viewportwidth };
        },
        render: function() {
        },
        renderPopup: function(educator, marker) {
            if (this.infowindow) {
                this.infowindow.close();
            }
            
            var offset = new google.maps.Size(-5, 15);
            var markup = this.educatorTemplate(educator.toTemplate());

            this.infowindow = new google.maps.InfoWindow({
                content: markup,
                maxWidth: 400});
            this.infowindow.open(this.mapInstance, marker);
            
            jQuery("div.educator-infowindow").parent().css("overflow", "hidden");
        },
        onAddEducator: function(educator) {
            var view = new EducatorPinView({
                model: educator,
                parentView: this
            });
        },
        onRemoveEducator: function(educator) {
            educator.destroy();
        },
        onResetEducators: function(collection, options) {
            var self = this;
            self.mapMarkers = [];
            if (self.markerClusterer) {
                self.markerClusterer.clearMarkers();
            }
            
            collection.forEach(function(obj) {
                var view = new EducatorPinView({
                    model: obj,
                    parentView: self
                });
                self.mapMarkers.push(view.marker);
            });
            
            self.markerClusterer = new MarkerClusterer(self.mapInstance,
                                                       self.mapMarkers);
        },
        onResize: function() {
            var viewport = this.getVisibleViewport();
            jQuery("#map-canvas").css({
                'height': viewport.height + "px"
            });
        },
        toggleAccordion: function(event) {
            var prev = jQuery(event.currentTarget).prev();
            jQuery(prev).find('i').toggleClass('icon-plus-sign icon-minus-sign');
        },
        onClickCriteria: function(event) {
            while (this.educators.pop());
            
            var self = this;
            var queryParams = "";
            var criteria = [];
            var searchCriteria = jQuery('.search_criteria:checked'); 
            searchCriteria.each(function() {
                queryParams += jQuery(this).attr('name') + 
                    "__in=" + jQuery(this).attr('value') + "&";
                criteria.push({
                    'name': jQuery(this).attr('name'),
                    'value': jQuery(this).attr('value'),
                    'display_name': jQuery(this).next().html()
                });
            });
            this.educators.queryParams = queryParams;
            this.educators.fetch();
            
            var markup = this.breadcrumbTemplate({'criteria': criteria});
            jQuery("ul.selected_criteria").html(markup);

        },
        onRemoveCriteria: function(evt) {
            var srcElement = evt.srcElement || evt.target || evt.originalTarget;
            var elt = jQuery(srcElement).find('input[type=hidden]');
            
            jQuery('[name="' + jQuery(elt).attr('name') + '"]' + 
                   '[value="' + jQuery(elt).attr('value') + '"]').trigger('click');
        }
    });
    
}(jQuery));    