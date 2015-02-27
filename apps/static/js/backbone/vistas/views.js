var app = app || {};


app.mainView = Backbone.View.extend({
    el: '#app',

    events: {
        'keyup #search-box': 'searchBox',
        'click .categories, .categories-all': 'selectCategories',
        'click .payments, .payments-all': 'selectPayments',
        'click .city, .city-all': 'selectCity',
        'click .btn-load': 'populateCallection',
    },
    initialize: function(){
        this.resultsCollection = new restaurants();
        this.resultsCollection.on('add', this.addRestaurant);
        this.timeLoad;
        this.next = null;
        this.count = 0;
        this.populateCallection();
        this.infinitScroll();
    },
    populateCallection: function(){
        var self = this;
        cage = new app.restaurant({page: self.next});
        cage.fetch({
            wait: true,
            success: function(models){
                var results = models.get('results');
                self.resultsCollection.add(results);
                self.next = models.get('next');
                self.count = models.get('count');

                if ( self.resultsCollection.length == self.count && self.count ){
                    $('.btn-load').addClass('invisible');
                }
            }
        });

    },
    searchBox: function(){
        var inputSearch = $('#search-box').val();
        $('.list-group').html('');
        if (inputSearch) {
            _.each(this.resultsCollection.byName(inputSearch), function(model){
                var vista = new app.restaurantView({model: model});
                $('.list-group').append(vista.render().$el);
            });
        } else {

            _.each(this.resultsCollection.allFilter(), function(model){
                var vista = new app.restaurantView({model: model});
                $('.list-group').append(vista.render().$el);
            });
        }
    },
    addRestaurant: function(modelo){
        if ($('#search-box').val()){
            this.searchBox;
        } else {
            var vista = new app.restaurantView({model: modelo});
            $('.list-group').append(vista.render().$el);
        }
    },
    infinitScroll: function(){
        var self = this;
        $(window).scroll(function(){
            if($(window).height() + $(window).scrollTop() == $(document).height()){
                if ( self.resultsCollection.length != self.count ){
                    self.populateCallection();
                }
            }
        });
    },
    selectCategories: function(ev){
        var categoriesAll = this.$('.categories-all');
        var categories = this.$('.categories:checked');
        var values = []

        if (ev.target.className == "categories-all"){
            categoriesAll.prop('checked', true);
            categoriesAll.attr('checked', true);
            categories.removeAttr('checked');
        } else {

             if (categories.length != this.$('.categories').length && categories.length) {
                categoriesAll.removeAttr('checked');
                categories.each(function() {
                    values.push(parseInt($(this).val()));
                });
            } else {
                categoriesAll.prop('checked', true);
                categoriesAll.attr('checked', true);
                categories.removeAttr('checked');
            }
        }
        this.resultsCollection.categories = values;
        this.searchBox();

    },
    selectPayments: function(ev){
        var paymentsAll = this.$('.payments-all');
        var payments = this.$('.payments:checked');
        var values = []

        if (ev.target.className == "payments-all"){
            paymentsAll.prop('checked', true);
            paymentsAll.attr('checked', true);
            payments.removeAttr('checked');
        } else {
            if (payments.length != this.$('.payments').length && payments.length) {
                paymentsAll.removeAttr('checked');
                payments.each(function() {
                    values.push(parseInt($(this).val()));
                });
            } else {
                paymentsAll.prop('checked', true);
                paymentsAll.attr('checked', true);
                payments.removeAttr('checked');
            }
        }
        this.resultsCollection.payments = values;
        this.searchBox();

    },
    selectCity: function(ev){
        var value = ev.target.value;
        this.resultsCollection.city = value;
        this.searchBox();

    },
});


app.restaurantView = Backbone.View.extend({
    template: _.template($('#tplRestaurant').html()),
    render: function(){
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    },

});