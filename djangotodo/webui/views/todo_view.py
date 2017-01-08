from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse

from webui.models.task import Task
from webui.models.status import Status
from webui.forms.task_form import TaskCreateForm

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

        task = Task()
        # Taskを新規作成するためのフォームを追加
        form = TaskCreateForm(instance=task)
        # return render(request, 'webui/todo.html', {'tasks': tasks})
        return render(request, 'webui/todo.html', dict(form=form, tasks=tasks))

    def post(self, request):
        """
        Create the new task.
        """
        # Insert the process to create task here.
        print(str(request.POST['status']))
        name = request.POST['name']
        memo = request.POST['memo']
        # status = request.POST['status']
        status = Status.objects.get(id=request.POST['status'])
        task = Task.create(name, memo, status)
        task.save()

        # 一覧表示用のデータを取得
        tasks = Task.objects.all()
        # Taskを新規作成するためのフォームを追加
        form = TaskCreateForm(instance=task)
        return render(request, 'webui/todo.html', dict(form=form, tasks=tasks))

class TodoListView(View):
    """
    List up the list of Todo
    """
    def get(self, request):
        """Return the list of to do(plan)"""
        # return HttpResponse('Todoの一覧')
        tasks = Task.objects.all()
        return render(request, 'webui/todo_list.html', {'tasks': tasks})



