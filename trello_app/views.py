from django.shortcuts import render, redirect
from .models import Task, TaskList
from .forms import TaskListForm, TaskForm
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    task_lists = TaskList.objects.all()
    return render(request, 'trello_app/index.html', {"tasks": tasks, "task_lists": task_lists})


def add_task_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        created_at = request.POST['created_at']
        task_list = TaskList(name=name, created_at=created_at, user1=request.user)
        task_list.save()
        return redirect('/')
    return render(request, 'trello_app/add_task_list.html')


def add_task_list_2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('/')
    else:
        form = TaskListForm()
    return render(request, 'trello_app/add_task_list_2.html', {'form': form})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'trello_app/add_task.html', {'form': form})
