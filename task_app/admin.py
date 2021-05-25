from django.contrib import admin
from task_app.models import Task


class TaskAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Task, TaskAdmin)
