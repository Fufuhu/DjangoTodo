from django.db import models


class Task(models.Model):
    """
    Task to do.
    """
    name = models.CharField(max_length=30)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    memo = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='Not started')

