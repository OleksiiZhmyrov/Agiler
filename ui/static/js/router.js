$(document).ready(function(){
    var SettingsRouter = Backbone.Router.extend ({
        routes: {
            '' : 'homePage',
            'settings/sprints': 'sprintsPage'
        },
        homePage: function () {
            hideAllPages();
        },
        sprintsPage: function () {
            hideAllPages();
            renderSprints();
        }
    });
    var appRouter = new SettingsRouter();
    Backbone.history.start();
});