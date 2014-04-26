var MenuBoardView = Backbone.View.extend({
    render: function () {
        this.el = ich.menuBoardsList(this.model.toJSON());
        return this;
    }
});

var MenuBoardsView = Backbone.View.extend({
    tagName: 'li',
    className: 'item',

    initialize: function () {
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
            $(this.el).append(new MenuBoardView({model: board}).render().el);
        }, this);

        return this;
    }
})

var menuBoardsView = new MenuBoardsView();

$(function () {
    $('#menu-boadrs-list').prepend(menuBoardsView.render().el);
});