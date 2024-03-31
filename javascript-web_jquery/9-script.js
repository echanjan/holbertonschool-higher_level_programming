$(document).ready(function () {
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    dataType: "json",
    success: function (response) {
      $("DIV#hello").text(response.hello);
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
    },
  });
});
