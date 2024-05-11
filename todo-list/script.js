const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

function addTask(){
    if(inputBox.value ==='') {
        alert("You must write something.");
    }
    else{
        let li = document.createElement("li")
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
        console.log(li)
    }
    inputBox.value = '';
    saveData();
    modal.style.display = "none"
}

listContainer.addEventListener("click", function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

// browser storage 
function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}
function showTasks(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTasks();

var modal = document.getElementById("todoModal");

var btn = document.getElementById("modalButton");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}