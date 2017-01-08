from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

from webui.models.task import Task

class TodoListView(View):
    """
    List up the list of Todo
    """
    def get(self, request):
        """Return the list of to do(plan)"""
        # return HttpResponse('Todoの一覧')
        tasks = Task.objects.all()
        return render(request, 'webui/todo_list.html', {'tasks': tasks})



