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
    $('div#notif-panel a.dropdown-toggle').on('mouseup', function (e) {
        $(this).parent().toggleClass('open');
        e.stopPropagation();
    });

    // Toggle message and notifications panel
    $('div#msg-panel a.dropdown-toggle').on('mouseup', function (e) {
        $(this).parent().toggleClass('open');
        e.stopPropagation();
    });

    // // Close message and notifications panel when clicking anywhere else
    // $('body').on('mouseup', function (e) {
    //     var notifIcon = $('div#notif-panel a.dropdown-toggle');
    //     var msgIcon = $('div#msg-panel a.dropdown-toggle');
    //     var socialDropdown = $('.dropdown-menu');
    //     if (!notifIcon.is(e.target)) {
    //         notifIcon.parent().removeClass('open');
    //     }
    //     if (!msgIcon.is(e.target)) {
    //         msgIcon.parent().removeClass('open');
    //     }
    // });

});

