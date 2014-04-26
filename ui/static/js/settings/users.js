var UserView = Backbone.View.extend({
    render: function () {
        this.el = ich.usersList(this.model.ToJSONwithFormattedDate());
        return this;
    }
});

var UserCollection = Backbone.Collection.extend({
    model: User,
    url: '/api/ws100/core/users/',

    parse: function (response) {
        return response.results;
    }
});

var UsersView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function () {
        this.boards = new UserCollection();
        this.boards.bind('sync', this.render, this);
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
        this.boards.each(function (user) {
            $(this.el).append(new UserView({model: user}).render().el);
        }, this);

        return this;
    }
})

var users = new UsersView();

function renderUsers() {
    users.fetch();
    $('#users-list').append(users.render().el);
    $('#page-users').show();
}
