const taskInput = document.getElementById("taskInput") as HTMLInputElement;
const addTaskButton = document.getElementById("addTaskButton") as HTMLButtonElement;
const taskList = document.getElementById("taskList") as HTMLUListElement;
const errorMessage = document.getElementById("errorMessage") as HTMLDivElement;

function addTask(): void {
    const taskText = taskInput.value.trim();

    if (taskText === "") {
        errorMessage.textContent = "Veuillez entrer une tâche !";
        return;
    }

    errorMessage.textContent = "";

    const taskItem = document.createElement("li");
    taskItem.textContent = taskText;

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Supprimer";
    deleteButton.addEventListener("click", () => {
        taskList.removeChild(taskItem); 
    });

    taskItem.appendChild(deleteButton);
    
    taskList.appendChild(taskItem);

    taskInput.value = "";
}

addTaskButton.addEventListener("click", addTask);
