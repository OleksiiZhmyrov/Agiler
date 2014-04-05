var User = Backbone.Model.extend({
    ToJSONwithFormattedDate: function() {
        var attr = _.clone(this.attributes);
        if(attr.date_joined) {
            attr.date_joined = moment(attr.date_joined).format('DD-MM-YYYY');
        }
        return attr;
    }
});

var UserView = Backbone.View.extend({
    render: function () {
        this.el = ich.usersList(this.model.ToJSONwithFormattedDate());
        return this;
    }
});

var UserCollection = Backbone.Collection.extend({
    model: User,
    url: '/api/ws100/core/users/',

    parse: function(response) {
        return response.results;
    }
});

var UsersView = Backbone.View.extend({
    tagName: 'tbody',

    initialize: function() {
        this.boards = new UserCollection();
        this.boards.bind('sync', this.render, this);
    },

    fetch: function() {
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

function renderUsers(){
    users.fetch();
    $('#users-list').append(users.render().el);
    $('#page-users').show();
}
