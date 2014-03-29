$(document).ready(function(){
    var SettingsRouter = Backbone.Router.extend ({
        routes: {
            '' : 'homePage',
            'settings/teams': 'teamsPage',
            'settings/sprints': 'sprintsPage'
        },
        homePage: function () {
            hideAllPages();
        },
        teamsPage: function () {
            hideAllPages();
            renderTeams();
        },
        sprintsPage: function () {
            hideAllPages();
            renderSprints();
        }
    });
    var appRouter = new SettingsRouter();
    Backbone.history.start();
});