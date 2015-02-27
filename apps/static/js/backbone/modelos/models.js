var app = app || {};

app.restaurant = Backbone.Model.extend({
    initialize: function(options){

        if (options){
            this.page = options.page;
        }

    },
    url: function(){
        if (this.page) {
           return  this.page;
        } else {
           return  '/api/restaurants/';
        }
    },
});
