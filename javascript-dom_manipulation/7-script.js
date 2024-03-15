fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    if (response.ok) return response.json();
  })
  .then((data) => {
    const titleArray = data.results.map((film) => film.title);
    titleArray.forEach((title) => {
      let list_movies = document.getElementById("list_movies");
      let li = document.createElement("li");
      li.innerText = title;
      list_movies.appendChild(li);
    });
  })
  .catch((error) => {
    console.error(error);
  });
