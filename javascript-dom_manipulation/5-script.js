const header = document.querySelector("header")
const newTextButton = document.getElementById("update_header")

newTextButton.addEventListener("click", function(){
    header.innerText= "New Header!!!";
});