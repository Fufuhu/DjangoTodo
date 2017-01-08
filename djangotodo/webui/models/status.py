"""
Model for status
"""
from django.db import models

class Status(models.Model):
    """
    Status for Task
    """
    name = models.CharField('ステータス', mex_length=30, blank=False, default='未着手')