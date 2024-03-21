from django.shortcuts import render
from .models import Todo

# Create your views here.
def todo(request):
    # todos = Todo.objects.all()
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    return render(request,"todo/todo.html",{"todos":todos})

def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id = id)
    except Exception as e:
        print(e)
    return render(request,"todo/view-todo.html",{"todo":todo})