/**
 * Created by noctule on 18.03.14.
 */
// load the following using JQuery's document ready function
$(function(){

    // Team model
    var Team = Backbone.Model.extend({});

    // set up the view for a team
    var TeamView = Backbone.View.extend({
        render: function () {
            // template with ICanHaz.js (ich)
            this.el = ich.teamRowTpl(this.model.toJSON());
            return this;
        }
    });

    // define the collection of teams
    var TeamCollection = Backbone.Collection.extend({
        model: Team,
        url: '/api/ws100/core/teams/',

        parse: function(response) {
            return response.results;
  }
    });

    // main app
    var AppView = Backbone.View.extend({
        tagName: 'tbody',

        initialize: function() {
            // instantiate a teams collection
            this.teams = new TeamCollection();
            this.teams.bind('all', this.render, this);
            this.teams.fetch();
        },

        render: function () {
            // template with ICanHaz.js (ich)
            this.$el.empty()  // clean teams list
            this.teams.each(function (team) {
                $(this.el).append(new TeamView({model: team}).render().el);
            }, this);

            return this;
        }
    })

    var app = new AppView();
    $('#app').append(app.render().el);
});