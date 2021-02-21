from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, related_name='Task',on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    Completion_date = models.DateField(null=True, blank=True)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name