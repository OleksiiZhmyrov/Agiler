$(function(){

    var Sprint = Backbone.Model.extend({});

    var SprintView = Backbone.View.extend({
        render: function () {
            this.el = ich.sprintsList(this.model.toJSON());
            return this;
        }
    });

    var SprintCollection = Backbone.Collection.extend({
        model: Sprint,
        url: '/api/ws100/core/sprints/',

        parse: function(response) {
            return response.results;
  }
    });

    var AppView = Backbone.View.extend({
        tagName: 'tr',

        initialize: function() {
            this.boards = new SprintCollection();
            this.boards.bind('all', this.render, this);
            this.boards.fetch({
                error: (function (e) {
                alert(' Service request failure: ' + e);
            })
            });
        },

        render: function () {
            this.$el.empty();
            this.boards.each(function (sprint) {
                $(this.el).append(new SprintView({model: sprint}).render().el);
            }, this);

            return this;
        }
    })

    var app = new AppView();
    $('#sprints-list').append(app.render().el);
    $('#page-sprints').show();
});