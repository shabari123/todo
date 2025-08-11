from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Todo.objects.create(title=title)
        return redirect("todo_list")
    return render(request, "todo_list.html", {"todos": todos})


def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")
