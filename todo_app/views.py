from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm  # Assuming you have a form for Todo (TodoForm)

# View to display all todos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# View to create a new todo
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the todo with the date
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

# View to edit an existing todo
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the todo list after saving
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/todo_edit.html', {'form': form, 'todo': todo})

# View to toggle completion of a todo
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed  # Toggle the completion status
    todo.save()
    return redirect('todo_list')

# View to delete a todo
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
