var Sprint = Backbone.Model.extend({
    ToJSONwithFormattedDate: function() {
        var attr = _.clone(this.attributes);
        if(attr.start_date) {
            attr.start_date = moment(attr.start_date).format('DD-MM-YYYY');
        }
        if(attr.finish_date) {
            attr.finish_date = moment(attr.finish_date).format('DD-MM-YYYY');
        } 
        return attr;
    }
});

var SprintView = Backbone.View.extend({
    render: function () {
        this.el = ich.sprintsList(this.model.ToJSONwithFormattedDate());
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

var SprintsView = Backbone.View.extend({
    tagName: 'tbody',

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

var sprints = new SprintsView();

function renderSprints(){
    $('#sprints-list').append(sprints.render().el);
    $('#page-sprints').show();
}
