var taskInput = document.getElementById("taskInput");
var addTaskButton = document.getElementById("addTaskButton");
var taskList = document.getElementById("taskList");
var errorMessage = document.getElementById("errorMessage");
function addTask() {
    var taskText = taskInput.value.trim();
    if (taskText === "") {
        errorMessage.textContent = "Veuillez entrer une tâche !";
        return;
    }
    errorMessage.textContent = "";
    var taskItem = document.createElement("li");
    taskItem.textContent = taskText;
    var deleteButton = document.createElement("button");
    deleteButton.textContent = "Supprimer";
    deleteButton.addEventListener("click", function () {
        taskList.removeChild(taskItem);
    });
    taskItem.appendChild(deleteButton);
    taskList.appendChild(taskItem);
    taskInput.value = "";
}
addTaskButton.addEventListener("click", addTask);
