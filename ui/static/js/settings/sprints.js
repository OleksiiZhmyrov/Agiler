var SprintView = Backbone.View.extend({
    render: function () {
        this.el = ich.sprintsList(this.model.ToJSONwithFormattedDate());
        return this;
    }
});

var SprintCollection = Backbone.Collection.extend({
    model: Sprint,
    url: '/api/ws100/core/sprints/',

    parse: function (response) {
        return response.results;
    }
});

var SprintsView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function () {
        this.boards = new SprintCollection();
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
        this.boards.each(function (sprint) {
            $(this.el).append(new SprintView({model: sprint}).render().el);
        }, this);

        return this;
    }
})

var sprints = new SprintsView();

function renderSprints() {
    sprints.fetch();
    $('#sprints-list').append(sprints.render().el);
    $('#page-sprints').show();
}
