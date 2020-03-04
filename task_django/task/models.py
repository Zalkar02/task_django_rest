from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name