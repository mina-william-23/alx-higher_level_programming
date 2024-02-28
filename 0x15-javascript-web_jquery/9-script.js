const api_url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(api_url, function (data, textStatus) {
  if (textStatus === 'success') {
    $('#hello').text(data.hello);
  }
});
