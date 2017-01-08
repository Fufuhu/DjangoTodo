from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

from webui.models.task import Task

class TodoView(View):
    """
    Set up, create, modify the task.
    """
    def get(self, request):
        """
        Create or modify the task.
        When there were no request_id setting,
        create the new task. When there is a task_id,
        modify the existing task.
        """
        tasks = Task.objects.all()
        return render(request, 'webui/todo.html', {'tasks': tasks})
    
    def post(self, request):
        tasks = Task.objects.all()
        # Insert the process to create task here.
        return render(request, 'webui/todo.html', {'tasks': tasks})

class TodoListView(View):
    """
    List up the list of Todo
    """
    def get(self, request):
        """Return the list of to do(plan)"""
        # return HttpResponse('Todoの一覧')
        tasks = Task.objects.all()
        return render(request, 'webui/todo_list.html', {'tasks': tasks})



