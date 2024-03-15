const newCharacter = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/4/?format=json")
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    newCharacter.innerText = data.name;
  })
  .catch((error) => {
    console.error("Error:", error);
  });
