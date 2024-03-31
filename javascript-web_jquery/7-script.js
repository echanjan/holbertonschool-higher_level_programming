$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    method: "GET",
    dataType: "json",
    success: function (response) {
      $("DIV#character").text(response.name);
    },
    error: function (xhr, status, error) {
      console.error("Error", error);
    },
  });
});
