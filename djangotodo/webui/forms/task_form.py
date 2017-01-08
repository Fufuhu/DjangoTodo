from django.forms import ModelForm
from webui.models.task import Task

class TaskCreateForm(ModelForm):
    """
    Form class for Task model
    """
    class Meta:
        model = Task
        fields = ('name', 'memo', )
