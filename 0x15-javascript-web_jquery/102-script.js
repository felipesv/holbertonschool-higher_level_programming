$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    $.ajax({
      type: 'GET',
      url: 'https://fourtonfish.com/hellosalut/',
      data: {
        lang: $('INPUT#language_code').val()
      },
      success: function (outmsg) {
        $('DIV#hello').html(outmsg.hello);
      }
    });
  });
});
