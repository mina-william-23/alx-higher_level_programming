const api_url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(api_url, function (data, textStatus) {
  if (textStatus === 'success') {
    $('#character').text(data.name);
  }
});
