from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task')
    status = models.BooleanField(default=True)
    repetitive = models.BooleanField(default=True)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
