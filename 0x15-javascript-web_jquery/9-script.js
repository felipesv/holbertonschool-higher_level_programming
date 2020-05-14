$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (outmsg) {
      $('DIV#hello').html(outmsg.hello);
    }
  });
});
