from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from todo.models import Task


def addTask(request):
    task = request.POST['task']
    if task =="":
        message="the task most be given"
    else:
        Task.objects.create(task = task)

    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_incomplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task,pk=pk)

    return render(request, 'edit_task.html')