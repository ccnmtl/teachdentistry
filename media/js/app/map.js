(function (jQuery) {       
    
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
            
            this.marker = new google.maps.Marker({
                position: this.latlng, 
                title: this.model.get('name'),
                map: this.parentView.mapInstance,
                icon: 'http://teachdentistry.org/site_media/img/blue-dot.png'
             });
            
            google.maps.event.addListener(this.marker, 'click', function() {
                self.parentView.trigger("markerClicked", self.model, self.marker);
            });
        },
        unrender: function () {
            
        }
    });
    
    window.EducatorMapView = Backbone.View.extend({
        events: {
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
                      "toggleAccordion");
            
            this.educatorTemplate =
                _.template(jQuery("#educator-template").html());

            this.educators = new EducatorList();
            this.educators.on("add", this.onAddEducator);
            this.educators.on("remove", this.onRemoveEducator);
            this.educators.on("reset", this.onResetEducators);
            this.educators.fetch();
            
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
            
            this.on("markerClicked", this.renderPopup);
            
            jQuery(window).trigger("resize");
        },
        getVisibleViewport: function() {
            var viewportwidth;
            var viewportheight;
            
            // the more standards compliant browsers (mozilla/netscape/opera/IE7) use window.innerWidth and window.innerHeight
            if (typeof window.innerWidth != 'undefined') {
                 viewportwidth = window.innerWidth;
                 viewportheight = window.innerHeight;
            } else if (typeof document.documentElement !== 'undefined' &&
                 typeof document.documentElement.clientWidth !=
                'undefined' && document.documentElement.clientWidth !== 0) {
                // IE6 in standards compliant mode (i.e. with a valid doctype as the first line in the document)
                viewportwidth = document.documentElement.clientWidth;
                viewportheight = document.documentElement.clientHeight;
            } else {
                // older versions of IE
                viewportwidth = document.getElementsByTagName('body')[0].clientWidth;
                viewportheight = document.getElementsByTagName('body')[0].clientHeight;
            }
            
            return { height: viewportheight -
                        (30 + document.getElementById("site-header").clientHeight +
                                document.getElementById("primarynav").clientHeight),
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
            collection.forEach(function(obj) {
                var view = new EducatorPinView({
                    model: obj,
                    parentView: self
                });
            });
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
        }
    });
    
}(jQuery));    