(function (jQuery) {

    Educator = Backbone.Model.extend({
        urlRoot: '/_main/api/v1/educator/',
        toJSON: function() {
            return this.get('resource_uri');
        },
        toTemplate: function() {
            return _(this.attributes).clone();
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
    
    window.EducatorMapView = Backbone.View.extend({
        events: {
            'resize': 'onResize'          
        },
        initialize: function(options) {
            _.bindAll(this,
                      "render",
                      "onAddEducator",
                      "onRemoveEducator",                   
                      "onResize",
                      "getVisibleViewport");

            this.educators = new EducatorList(options.actors);
            this.educators.on("add", this.onAddEducator);
            this.educators.on("remove", this.onRemoveEducator);            
            this.educators.fetch();
            
            var mapOptions = {
                center: new google.maps.LatLng(39.8282, -98.5795),
                zoom: 4,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            
            var elt = document.getElementById("map-canvas");
            var mapInstance = new google.maps.Map(elt, mapOptions);
            
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
                        (30 + document.getElementById("masthead").clientHeight +
                                document.getElementById("primarynav").clientHeight),
                     width: viewportwidth };
        },
        render: function() {
            var self = this;

            // toggle map layers on/off
            jQuery(".career_location_map_layer").each(function() {
                var dataId = jQuery(this).data("id");
                if (self.state.get("layers").getByDataId(dataId) || self.state.get("view_type") === "BD") {
                    // Check layer box
                    jQuery("#select_layer_" + dataId).attr("checked", "checked");

                    // Display layer & legend
                    jQuery("#map_layer_" + dataId).show();
                    jQuery("#map_legend_" + dataId).show();
                } else {
                    // Uncheck layer box
                    jQuery("#select_layer_" + dataId).removeAttr("checked");

                    // Hide layer
                    jQuery("#map_layer_" + dataId).hide();
                    jQuery("#map_legend_" + dataId).hide();
                }
            });

            var selectedLayers = self.state.get("layers");
            if (selectedLayers.length > 0) {
                jQuery("div.map_legend_container h3").show();
            } else {
                jQuery("div.map_legend_container h3").hide();
            }

            if (this.state.get("view_type") === "IV" || this.state.get("view_type") === "LC") {
                this.renderStakeholderInterview();
            }
            if (this.state.get("view_type") === "LC" || this.state.get("view_type") === "BD") {
                this.renderSelectLocation();
            }
            if (this.state.get("view_type") === "BD") {
                this.renderBoardView();
            }
        },
        onResize: function() {
            var viewport = getVisibleViewport();
            jQuery("#map-canvas").css({
                'height': viewport.height + "px"
            });
        }        
    });
    
}(jQuery));    