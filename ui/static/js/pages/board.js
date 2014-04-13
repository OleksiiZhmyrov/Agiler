
var BoardContainer = Backbone.Model.extend({
    urlRoot: '/api/ws100/retro/boards/',

    url: function() {
        return this.urlRoot +this.id +'/';
    }
});

var BoardContainerView = Backbone.View.extend({
    tagName: 'tbody',


    initialize: function(opts) {
        this.boardContainer = new BoardContainer({id:opts.pk});
        this.boardContainer.bind('sync', this.render, this);
    },

    fetch: function() {
        this.boardContainer.fetch({
            error: (function (e) {
                alert(' Service request failure: ' + e);
            })
        });
    },

    render: function () {
        clearBoardTables();
        $('#board-details').html(ich.boardDetails(this.boardContainer.toJSON()));
        $('table#stickers-was-good').append(ich.goodList({was_good: this.boardContainer.toJSON().was_good}));
        $('table#stickers-need-to-change').append(ich.changeList({need_to_change: this.boardContainer.toJSON().need_to_change}));
        $('table#stickers-action-points').append(ich.pointsList({action_point: this.boardContainer.toJSON().action_point}));
    }
});

function renderBoard(pk) {
    var boardContainer = new BoardContainerView({pk:pk});
    boardContainer.fetch();
    $('#board-page').show();
}

function clearBoardTables() {
    $('table#stickers-was-good tbody').empty();
    $('table#stickers-need-to-change tbody').empty();
    $('table#stickers-action-points tbody').empty();
}
