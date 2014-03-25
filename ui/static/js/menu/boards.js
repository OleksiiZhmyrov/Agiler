$(function(){

    var Board = Backbone.Model.extend({});

    var BoardView = Backbone.View.extend({
        render: function () {
            this.el = ich.boardsList(this.model.toJSON());
            return this;
        }
    });

    var BoardCollection = Backbone.Collection.extend({
        model: Board,
        url: '/api/ws100/retro/boards/',

        parse: function(response) {
            return response.results;
  }
    });

    var AppView = Backbone.View.extend({
        tagName: 'li',
        className: 'item',

        initialize: function() {
            this.boards = new BoardCollection();
            this.boards.bind('all', this.render, this);
            this.boards.fetch({
                error: (function (e) {
                alert(' Service request failure: ' + e);
            })
            });
        },

        render: function () {
            this.$el.empty();
            this.boards.each(function (board) {
                $(this.el).append(new BoardView({model: board}).render().el);
            }, this);

            return this;
        }
    })

    var app = new AppView();
    $('#boadrs-list').prepend(app.render().el);

});