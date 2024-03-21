from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField(blank = True)
    created = models.DateField(auto_now_add = True)
    date_completed = models.DateTimeField(blank = True, null = True)
    important = models.BooleanField(default = False)

    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id}-{self.created}-{self.title}-{self.user}"