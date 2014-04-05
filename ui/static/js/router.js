$(document).ready(function(){
    var SettingsRouter = Backbone.Router.extend ({
        routes: {
            '': 'homePage',
            'boards/:pk': 'boardPage',
            'settings/users': 'usersPage',
            'settings/teams': 'teamsPage',
            'settings/sprints': 'sprintsPage'
        },
        homePage: function () {
            hideAllPages();
        },
        boardPage: function (pk) {
            hideAllPages();
            renderBoard(pk);
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