$(document).ready(function(){
    var SettingsRouter = Backbone.Router.extend ({
        routes: {
            '': 'homePage',
            'boards/:pk': 'boardPage',
            'boards': 'boardsPage',
            'settings/users': 'usersPage',
            'settings/teams': 'teamsPage',
            'settings/sprints': 'sprintsPage',
            '*notFound': 'notFound'
        },
        homePage: function () {
            hideAllPages();
        },
        boardPage: function (pk) {
            hideAllPages();
            renderBoard(pk);
        },
        boardsPage: function () {
            hideAllPages();
            renderBoards();
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
        },
        notFound: function () {
            display_404();
        }
    });
    var appRouter = new SettingsRouter();
    Backbone.history.start();
});