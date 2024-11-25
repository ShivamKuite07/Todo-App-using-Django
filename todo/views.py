from django.shortcuts import render, redirect, get_object_or_404
from .models import Todos
from django.http import HttpResponse

# Create your views here.

def index(request):
    todos = Todos.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, 'index.html', context)

def addtodo(request):
    if request.method == 'POST':
        message = request.POST['message']
        new_message = Todos.objects.create(message=message)
        new_message.save()

    return redirect('/')

def deletetodo(request, id):
    todo = get_object_or_404(Todos, id=id)
    todo.delete()
    return redirect('/')

def edittodo(request, id):
    todo = get_object_or_404(Todos, id=id)
    if request.method == 'POST':
        new_message = request.POST['message']
        todo.message = new_message
        todo.save()
        return redirect('/')
    return redirect('/')