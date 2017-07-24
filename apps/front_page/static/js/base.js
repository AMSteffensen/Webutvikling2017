// Repsonsible for securing scripts
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// Keep SideNav collapse open on refresh (WORK IN PROGRESS)
$(document).ready(function () {
    var loc = location.pathname.split("/");
    $('#menu-content a[href*="/' + loc[loc.length - 3] + "/" + loc[loc.length - 2] + '/"]').parents("ul:first").attr("aria-expanded", true).addClass("in");


    // Toggle message and notifications panel
    $('div#notif-panel a.dropdown-toggle').click(function (e) {
        $(this).parent().toggleClass('open');
    });

    // Toggle message and notifications panel
    $('div#msg-panel a.dropdown-toggle').click(function (e) {
        $(this).parent().toggleClass('open');
    });

    // // Close message and notifications panel when clicking anywhere else
    // $('body').on('click', function (e) {
    //     var socialIcon = $('div#notif-panel');
    //     if (!socialIcon.is(e.target)) {
    //         socialIcon.removeClass('open');
    //     }
    // });

});

