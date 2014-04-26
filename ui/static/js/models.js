var Sticker = Backbone.Model.extend({
    schema: {
        type: { type: 'Select', title: 'Type', options: ['G', 'C', 'A'] },
        summary: { type: 'Text', title: 'Summary' }
    }
});

var Board = Backbone.Model.extend({
    ToJSONWithExtraFields: function () {
        var attr = _.clone(this.attributes);
        if (attr.isActive) {
            attr.isActiveColumn = { value: "active", class: "label label-success" };
        } else {
            attr.isActiveColumn = { value: "closed", class: "label label-default" };
        }
        return attr;
    }
});

var Sprint = Backbone.Model.extend({
    ToJSONwithFormattedDate: function () {
        var attr = _.clone(this.attributes);
        if (attr.start_date) {
            attr.start_date = moment(attr.start_date).format('DD-MM-YYYY');
        }
        if (attr.end_date) {
            attr.end_date = moment(attr.end_date).format('DD-MM-YYYY');
        }
        return attr;
    }
});

var Team = Backbone.Model.extend({

});

var User = Backbone.Model.extend({
    ToJSONwithFormattedDate: function () {
        var attr = _.clone(this.attributes);
        if (attr.date_joined) {
            attr.date_joined = moment(attr.date_joined).format('DD-MM-YYYY');
        }
        if (attr.is_active) {
            attr.statusColumn = { value: "active", class: "label label-success" };
        } else {
            attr.statusColumn = { value: "inactive", class: "label label-danger" };
        }
        return attr;
    }
});

var Settings = Backbone.Model.extend({
    urlRoot: '/api/ws100/core/settings/'
});