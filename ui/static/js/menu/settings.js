$(function(){

    var Settings = Backbone.Model.extend({
        urlRoot: '/api/ws100/core/settings/'
    });

    var SettingsView = Backbone.View.extend({
                tagName: 'li',
        className: 'item',

        initialize: function() {
            this.setting = new Settings();
                                                //console.log(this)

            this.setting.bind('sync', this.render, this);
            this.setting.fetch();
                                    //console.log(this.setting)
        },

        render: function () {
            //console.log(this.setting.toJSON())
            //this.el = ich.settingsList(this.setting.toJSON());
            $('#settings-list').html(ich.settingsList(this.setting.toJSON()));
                        //console.log(this)
            //return this;
        }
    });

    var settings = new SettingsView();
    //console.log(settings.render())
        //console.log(settings.render().el)

//    console.log(settings.render().el);
//    console.log($('#settings-list').append(settings.render().el));
   //$('#settings-list').html(settings.render().el);

});