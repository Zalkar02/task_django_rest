from django.db import models
from task.models import Task 

class Tag(models.Model):
    name = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now=True)
    tasks = models.ManyToManyField(Task, related_name='tags')
    