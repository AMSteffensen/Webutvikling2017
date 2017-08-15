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

$(document).ready(function () {


    // Keep SideNav collapse open on refresh
    var loc = location.pathname;
    submenu = $('#menu-content a[href*="' + loc + '"]');
    submenu.parents("li:first").addClass("active");
    submenu.parents("ul:first").attr("aria-expanded", true).addClass("in").prev().addClass("active");
    //user, users


    // TOGGLE SOCIAL NOTIFICATIONS PANEL ------------------------------
    // Toggle message and notifications panel
    $('div#notif-panel a.dropdown-toggle').on('mouseup', function (e) {
        $('div#msg-panel a.dropdown-toggle').parent().removeClass('open');
        $(this).parent().toggleClass('open');
        e.stopPropagation();
    });

    // Toggle message and notifications panel
    $('div#msg-panel a.dropdown-toggle').on('mouseup', function (e) {
        $('div#notif-panel a.dropdown-toggle').parent().removeClass('open');
        $(this).parent().toggleClass('open');
        e.stopPropagation();
    });

    // Close message and notifications panel when clicking anywhere else
    $('body').on('mouseup', function (e) {
        var socialIcon = $('a.dropdown-toggle');
        var socialDropdown = $('.dropdown-menu');
        if (!socialIcon.is(e.target) && !socialDropdown.is(e.target) && !socialDropdown.has(e.target).length > 0) {
            socialIcon.parent().removeClass('open');
        }
    });

    // Toggle visibility for close button in notification panel

    jQuery(document).ready(function() {
      jQuery('.btnDelete').css('visibility', 'hidden');
    });
    jQuery(document).ready(function() {
      jQuery('.notificationMargin').hover(function() {
        jQuery(this).find('.btnDelete').css('visibility', 'visible');
        },
      function() {
        jQuery('.btnDelete').css('visibility', 'hidden');
        });
    });
    // TOGGLE SOCIAL NOTIFICATIONS PANEL ------------------------------
});
