from django.db import models

# Create your models here.
class Todo(models.Model):
    taskname = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname