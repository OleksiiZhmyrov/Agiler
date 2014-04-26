var BoardContainer = Backbone.Model.extend({
    urlRoot: '/api/ws100/retro/boards/',

    url: function () {
        return this.urlRoot + this.id + '/';
    },

    ToJSONWithFormattedDate: function () {
        var attr = _.clone(this.attributes);
        if (attr.sprint.start_date) {
            attr.start_date = moment(attr.sprint.start_date).format('DD-MM-YYYY');
        }
        if (attr.sprint.end_date) {
            attr.end_date = moment(attr.sprint.finish_date).format('DD-MM-YYYY');
        }
        return attr;
    }
});

var BoardContainerView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function (opts) {
        this.boardContainer = new BoardContainer({id: opts.pk});
        this.boardContainer.bind('sync', this.render, this);
    },
    fetch: function () {
        this.boardContainer.fetch({
            error: onErrorHandler
        });
    },
    render: function () {
        clearBoardTables();
        var json = this.boardContainer.ToJSONWithFormattedDate();
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
    var boardContainer = new BoardContainerView({pk: pk});
    boardContainer.fetch();
    $('#board-page').show();
}

function clearBoardTables() {
    $('table.table-stickers tbody tr.item').remove();
    $('table.table-stickers tbody tr.message').show();
}
