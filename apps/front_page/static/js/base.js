// Repsonsible for securing scripts
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});





// Keep SideNav collapse open on refresh (WORK IN PROGRESS)
$(document).ready(function() {
  var loc = location.pathname.split("/");
      $('#menu-content a[href*="/' + loc[loc.length -3] + "/" + loc[loc.length -2] + '/"]').parents("ul:first").attr("aria-expanded",true).addClass("in");
  });