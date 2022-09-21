from django.db import models


# Create your models here.



class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=100)

    def __str__(self):
        return self.name
