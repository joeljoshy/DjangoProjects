from django.db import models

# Create your models here.

class ToDo(models.Model):
    task_name = models.TextField()
    status = models.CharField(max_length=20)
    user = models.CharField(max_length=20)

    def __str__(self):
        return self.user