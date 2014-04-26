var BoardView = Backbone.View.extend({
    render: function () {
        this.el = ich.boardsList(this.model.ToJSONWithExtraFields());
        return this;
    }
});

var BoardCollection = Backbone.Collection.extend({
    model: Board,
    url: '/api/ws100/retro/boards/',

    parse: function (response) {
        return response.results;
    }
});

var BoardsView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function () {
        this.boards = new BoardCollection();
        this.boards.bind('all', this.render, this);
    },

    fetch: function () {
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

var boards = new BoardsView();

function renderBoards() {
    boards.fetch();
    $('#boards-list').append(boards.render().el);
    $('#page-boards').show();
}
