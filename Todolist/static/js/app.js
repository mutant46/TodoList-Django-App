var create_task = document.querySelector(".btn")
var form = document.querySelector(".createTask")
var cross = document.querySelector(".close")

function myfunction() {
    form.classList.add('toggle')
    form.classList.remove('toggle-up')
}

function closefunction() {
    form.classList.add("toggle-up")
    form.classList.remove('toggle')
}


create_task.addEventListener('click', myfunction)
cross.addEventListener('click', closefunction)