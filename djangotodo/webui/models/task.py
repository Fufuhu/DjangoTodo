"""
Model for Task
"""
from django.db import models
from datetime import datetime
from webui.models.status import Status



class Task(models.Model):
    """
    Task to do.
    """
    name = models.CharField('タスク名', max_length=30, blank=False)
    startTime = models.DateTimeField('開始時刻', blank=True)
    endTime = models.DateTimeField('終了時刻', blank=True, null=True)
    memo = models.CharField('メモ', max_length=200, blank=True)
    # status = models.CharField('状態', max_length=20, default='未着手', blank=False)
    status = models.ForeignKey(Status)

    def create(name, memo):
        task = Task()
        task.name = name
        task.memo = memo
        task.startTime = datetime.now()
        return task
