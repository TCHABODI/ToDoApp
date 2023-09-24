from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from todo.models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')
    #return render(request,'home.html')