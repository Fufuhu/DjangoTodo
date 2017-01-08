from django.contrib import admin
from webui.models.task import Task
from webui.models.status import Status

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startTime', 'endTime', 'status', 'memo', )
admin.site.register(Task, TaskAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
admin.site.register(Status, StatusAdmin)
