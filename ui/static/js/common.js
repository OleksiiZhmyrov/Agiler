function hideAllPages() {
    $('.app-page').hide();
}

function display_404() {
    hideAllPages();
    $('#404_app_page').show();
}

function display_error_dropdown() {
    var box = $('#alert-box');
    box.slideDown("slow");
    setTimeout(function () {
        box.slideUp("slow");
    }, 3000);
}

var onErrorHandler = function (collection, response, options) {
    display_404()
    display_error_dropdown();
    console.log(response.responseText);
};