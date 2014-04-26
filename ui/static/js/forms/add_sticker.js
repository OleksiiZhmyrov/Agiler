var addStickerFormTemplate = _.template($('#add_sticker_form_template').html())

var AddStickerForm = Backbone.Form.extend({
    schema: {
        type: { type: 'Select', title: 'Type', options: ['G', 'C', 'A'] },
        summary: { type: 'Text', title: 'Summary' }
    }
});

AddStickerForm.template = addStickerFormTemplate;

var form = new AddStickerForm({ model: new Sticker() }).render();

$('#add_form').html(form.el);