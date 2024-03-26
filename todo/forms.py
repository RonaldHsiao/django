from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    #  表單綁定資料模型
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ["title", "text", "important", "completed"]