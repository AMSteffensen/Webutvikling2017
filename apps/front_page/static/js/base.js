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

  <!-- Hide/show searchbar -->

    document.getElementById("searchBar").style.display = 'none';
      function hideShow() {

          var x = document.getElementById('searchBar');
          if (x.style.display === 'none') {
              x.style.display = 'block';
          } else {
              x.style.display = 'none';
          }
      }


  // localStorage.setItem('shownOnRefresh', JSON.stringify(shownOnRefresh));
  //
  // $('#brukere').on('shown.bs.collapse', '.panel-collapse', function() {
  //         shownOnRefresh = JSON.parse(localStorage.getItem('shownOnRefresh'));
  //         if ($.inArray($(this).attr('id'), shownOnRefresh) == -1) {
  //             shownOnRefresh.push($(this).attr('id'));
  //         };
  //         localStorage.setItem('shownOnRefresh', JSON.stringify(shownOnRefresh));
  // });
  //
  // $('#brukere').on('hidden.bs.collapse', '.panel-collapse', function() {
  //         shownOnRefresh = JSON.parse(localStorage.getItem('shownOnRefresh'));
  //         shownOnRefresh.splice( $.inArray($(this).attr('id'), shownOnRefresh), 1 );//remove item from array
  //         localStorage.setItem('shownOnRefresh', JSON.stringify(shownOnRefresh));
  // });
  //
  // // On page refresh
  // var shownOnRefresh = JSON.parse(localStorage.getItem('shownOnRefresh '));
  // for (var i in shownOnRefresh ) {
  //     $('#' + shownOnRefresh [i]).addClass('in');
  // }
