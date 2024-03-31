$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function (response) {
      $("ul#list_movies").empty();
      response.results.forEach(function (movie) {
        $("ul#list_movies").append("<li>" + movie.title + "</li>");
      });
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
    },
  });
});
