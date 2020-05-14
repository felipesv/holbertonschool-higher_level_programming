$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    contentType: 'json',
    success: function (outmsg) {
      outmsg.results.forEach(element => {
        $('UL#list_movies').append('<li>' + element.title + '</li>');
      });
    }
  });
});
