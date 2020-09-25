const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data) {
  const films = data.results;
  $.each(films, function (index, film) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
