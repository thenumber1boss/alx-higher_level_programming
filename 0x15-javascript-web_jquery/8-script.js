$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  console.log(data);
  data.results.forEach(film => {
    $('UL#list_movies').append(film.title);
  });
});
