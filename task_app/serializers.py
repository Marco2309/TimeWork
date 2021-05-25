from django.contrib.auth import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from task_app.models import Task


class TaskViewSeralizer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
