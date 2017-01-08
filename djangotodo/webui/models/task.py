"""
Model for Task
"""
from django.db import models



class Task(models.Model):
    """
    Task to do.
    """
    name = models.CharField('タスク名', max_length=30)
    startTime = models.DateTimeField('開始時刻')
    endTime = models.DateTimeField('終了時刻')
    memo = models.CharField('メモ', max_length=200)
    status = models.CharField('状態', max_length=20, default='未着手')

