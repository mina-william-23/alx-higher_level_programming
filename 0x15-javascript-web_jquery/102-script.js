// $(document).ready(function() === $(function ()
// it should wrap the code in a jQuery wrapper
$(function () {
  const url_api = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').click(function () {
    const lang_api = $('INPUT#language_code').val();
    $.get(url_api, {lang: lang_api}, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
