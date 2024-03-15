const header = document.querySelector("header");
const redHeader = document.getElementById("toggle_header");

toggle_header.addEventListener("click", function(){
    header.classList.toggle("red");
    header.classList.toggle("green");
}); 