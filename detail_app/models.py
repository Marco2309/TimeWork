from django.db import models
from task_app.models import Task
# Create your models here.


class Detail(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name='detail')
    invoice = models.IntegerField()
    type = models.CharField(max_length=10)
    date_time = models.CharField(max_length=200)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.type
