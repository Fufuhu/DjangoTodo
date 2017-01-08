"""
Model for status
"""
from django.db import models

class Status(models.Model):
    """
    Status for Task
    """
    name = models.CharField('ステータス', max_length=30, blank=False)

    def __str__(self):
        return self.name
