from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TaskcreationForm, TaskEditForm
from django.contrib.auth.decorators import login_required
from .models import Task
# Create your views here.


def Home(request):
    return render(request, 'html/home.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = TaskcreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskcreationForm()
    task = Task.objects.filter(user = request.user)
    task_sorted = task.order_by('completion_status')
    context = {
        'form' : form,
        'task' : task_sorted
    }
    return render(request, 'html/dashboard.html', context)

def deletetask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('dashboard')

def edittask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    data = {
        'name' : task.name,
        'description' : task.description,
        'Completion_date' : task.Completion_date
    }
    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=True)
            return redirect('dashboard')
            
    else:
        form = TaskEditForm(initial=data)
    context = {
        'form' : form
    }
    return render(request, 'html/edit-task.html', context)


def set_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completion_status = True
    task.save()
    return redirect('dashboard')

def profile(request):
    return render(request, 'html/profile.html')




