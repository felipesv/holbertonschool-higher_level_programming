$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    contentType: 'json',
    success: function (outmsg) {
      $('DIV#character').html(outmsg.name);
    }
  });
});
