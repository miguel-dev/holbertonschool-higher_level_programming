$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const filmList = data.results;
  $.each(filmList, function (i, film) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
