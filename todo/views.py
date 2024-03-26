from django.shortcuts import render
from .models import Todo
from .forms import TodoForm

def create_todo(request):
    message = ""
    form = TodoForm()
    if request.method == "POST":
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            message = "建立事項成功"
        except Exception as e:
            print(e)
            message = "建立事項失敗"
    return render(request,"todo/create-todo.html",{"form":form},{"message":message})


# Create your views here.
def todolist(request):
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