from django.contrib import admin
from webui.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startTime', 'endTime','status', 'memo',)
admin.site.register(Task, TaskAdmin)