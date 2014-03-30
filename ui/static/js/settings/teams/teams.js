var Team = Backbone.Model.extend({});

var TeamView = Backbone.View.extend({
    render: function () {
        this.el = ich.teamsList(this.model.toJSON());
        return this;
    }
});

var TeamsCollection = Backbone.Collection.extend({
    model: Team,
    url: '/api/ws100/core/teams/',

    parse: function(response) {
        return response.results;
    }
});

var TeamsView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function() {
        this.boards = new TeamsCollection();
        this.boards.bind('all', this.render, this);
        this.boards.fetch({
            error: (function (e) {
                alert(' Service request failure: ' + e);
            })
        });
    },

    render: function () {
        this.$el.empty();
        this.boards.each(function (team) {
            $(this.el).append(new TeamView({model: team}).render().el);
        }, this);

        return this;
    }
})

function renderTeams(){
    var teams = new TeamsView();

    $('#teams-list').html(teams.render().el);
    $('#page-teams').show();
}
