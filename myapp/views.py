from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form})

def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form})

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_edit.html', {'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo': todo})

def todo_toggle(request, id):
    task = Todo.objects.get(id=id)
    task.completed = not task.completed  # Toggle the completed status
    task.save()
    return redirect('todo_list')
