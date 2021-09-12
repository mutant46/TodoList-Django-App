from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
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
    task = Task.objects.filter(user=request.user)
    task_sorted = task.order_by('completion_status')
    context = {
        'form': form,
        'task': task_sorted
    }
    return render(request, 'html/dashboard.html', context)


def deletetask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('dashboard')


def edittask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    data = {
        'name': task.name,
        'description': task.description,
        'Completion_date': task.Completion_date
    }
    if request.method == "POST":
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save(commit=True)
            return redirect('dashboard')

    else:
        form = TaskEditForm(initial=data)
    context = {
        'form': form
    }
    return render(request, 'html/edit-task.html', context)


def set_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completion_status = True
    task.save()
    return redirect('dashboard')


def react_api(request):
    response = [
        {
            "id": 1,
            "title": "buttermilk pancakes",
            "category": "breakfast",
            "price": 15.99,
            "img": "./images/item-1.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 2,
            "title": "dinner double",
            "category": "lunch",
            "price": 13.99,
            "img": "./images/item-2.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 3,
            "title": "Godzilla milkshake",
            "category": "shakes",
            "price": 6.99,
            "img": "./images/item-3.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 4,
            "title": "country delight",
            "category": "breakfast",
            "price": 20.99,
            "img": "./images/item-4.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 5,
            "title": "egg attack",
            "category": "lunch",
            "price": 20.99,
            "img": "./images/item-5.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 6,
            "title": "buttermilk pancakes",
            "category": "breakfast",
            "price": 15.99,
            "img": "./images/item-6.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 7,
            "title": "bacon overdflow",
            "category": "breakfast",
            "price": 8.99,
            "img": "./images/item-7.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 8,
            "title": "american classic",
            "category": "lunch",
            "price": 12.99,
            "img": "./images/item-8.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        },
        {
            "id": 9,
            "title": "qurantine buddy",
            "category": "shakes",
            "price": 15.99,
            "img": "./images/item-9.jpeg",
            "desc": "I'm baby woke mlkshk wolf bitters live-edge blue bottle, hammock freegan copper mug whatever cold-pressed"
        }
    ]
    return JsonResponse(response, safe=False)
