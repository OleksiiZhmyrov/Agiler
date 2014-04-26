var TeamView = Backbone.View.extend({
    render: function () {
        this.el = ich.teamsList(this.model.toJSON());
        return this;
    }
});

var TeamsCollection = Backbone.Collection.extend({
    model: Team,
    url: '/api/ws100/core/teams/',

    parse: function (response) {
        return response.results;
    }
});

var TeamsView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function () {
        this.teams = new TeamsCollection();
        this.teams.bind('all', this.render, this);
    },

    fetch: function () {
        this.teams.fetch({
            error: (function (e) {
                alert(' Service request failure: ' + e);
            })
        });
    },

    render: function () {
        this.$el.empty();
        this.teams.each(function (team) {
            $(this.el).append(new TeamView({model: team}).render().el);
        }, this);

        return this;
    }
})

var teams = new TeamsView();

function renderTeams() {
    teams.fetch();
    $('#teams-list').append(teams.render().el);
    $('#page-teams').show();
}
