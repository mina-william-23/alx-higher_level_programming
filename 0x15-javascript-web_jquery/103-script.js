// $(document).ready(function() === $(function ()
// it should wrap the code in a jQuery wrapper
$(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keydown(function (event) {
    // Enter button keycode is 13
    if (event.keyCode === 13) {
      translate();
    }
  });
});

function translate() {
  const url_api = 'https://hellosalut.stefanbohacek.dev/';
  const lang_api = $('INPUT#language_code').val();
  $.get(url_api, {lang: lang_api}, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
