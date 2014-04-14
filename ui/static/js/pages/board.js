
var BoardContainer = Backbone.Model.extend({
    urlRoot: '/api/ws100/retro/boards/',

    url: function() {
        return this.urlRoot + this.id +'/';
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
        var json = this.boardContainer.toJSON();
        $('#board-details').html(ich.boardDetails(json));

        if (json.was_good.length != 0) {
            $('table#stickers-was-good tbody tr.message').hide();
            $('table#stickers-was-good').append(ich.goodList({was_good: json.was_good}));
        }
        if (json.need_to_change.length != 0) {
            $('table#stickers-need-to-change tbody tr.message').hide();
            $('table#stickers-need-to-change').append(ich.changeList({need_to_change: json.need_to_change}));
        }
        if (json.action_point.length != 0) {
            $('table#stickers-action-points tbody tr.message').hide();
            $('table#stickers-action-points').append(ich.pointsList({action_point: json.action_point}));
        }
    }
});

function renderBoard(pk) {
    var boardContainer = new BoardContainerView({pk:pk});
    boardContainer.fetch();
    $('#board-page').show();
}

function clearBoardTables() {
    $('table.table-stickers tbody tr.item').remove();
    $('table.table-stickers tbody tr.message').show();
}
