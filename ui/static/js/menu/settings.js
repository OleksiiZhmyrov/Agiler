$(function () {

    var SettingsView = Backbone.View.extend({
        tagName: 'li',
        className: 'item',

        initialize: function () {
            this.setting = new Settings();
            this.setting.bind('sync', this.render, this);
            this.setting.fetch({
                error: (function (e) {
                    alert(' Service request failure: ' + e);
                })
            });
        },

        render: function () {
            $('#settings-list').html(ich.settingsList(this.setting.toJSON()));
        }
    });

    var settings = new SettingsView();
});