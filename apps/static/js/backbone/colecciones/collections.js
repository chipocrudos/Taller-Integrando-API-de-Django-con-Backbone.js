var app = app || {};

var restaurants = Backbone.Collection.extend({
    model: app.restaurant,
    initialize: function(options){

        this.city = '';
        this.payments = [];
        this.categories = [];
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
    allFilter: function(){
        var self = this;
        return this.filter(function(model) {
            if ( self._excludeFilter(model) ) {
                return model;
            }
        });
    },
    byName: function(letters){
        if(letters == '') return this;
        var self = this;
        var pattern = new RegExp(letters,'gi');
        return this.filter(function(model) {
            if ( self._excludeFilter(model) ) {
                return pattern.test(model.get('name'));
            }
        });
    },
    _excludeFilter: function(model){
            return ( this._byPay(model) && this._byCategory(model) && this._byCity(model))
    },
    _byPay: function(model){
        var pay = true;
        var payment = model.get('payment');
        if (this.payments.length){
            pay = false;
            _.each(this.payments, function(value){
                if (payment.indexOf(value) != -1) {
                    pay = true;
                }
            });
        }
        return pay;
    },
    _byCategory: function(model){
        var cat = true;
        var category = model.get('category');
        if (this.categories.length){
            cat = false;
            _.each(this.categories, function(value){
                if (category.indexOf(value) != -1) {
                    cat = true;
                }
            });
        }
        return cat;
    },
    _byCity: function(model){
        var city = true;
        if (this.city){
            var city = false;
            var cities = model.get('cities');
            if (cities.indexOf(this.city) != -1) {
                city = true;
            }
        }
        return city;
    }


});

app.restaurantsCollection = new restaurants();