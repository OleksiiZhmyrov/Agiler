$(document).ready(function(){
    var SettingsRouter = Backbone.Router.extend ({
        routes: {
            '' : 'homePage',
            'settings/users': 'usersPage',
            'settings/teams': 'teamsPage',
            'settings/sprints': 'sprintsPage'
        },
        homePage: function () {
            hideAllPages();
        },
        usersPage: function () {
            hideAllPages();
            renderUsers();
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