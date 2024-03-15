const addItemButton = document.getElementById("add_item");
const list = document.querySelector(".my_list");

addItemButton.addEventListener("click", function() {
    const newItem = document.createElement("li");
    newItem.textContent = "Item";

    list.appendChild(newItem);
});