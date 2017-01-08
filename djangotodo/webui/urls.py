from django.conf.urls import url
from webui.views.todo_view import TodoListView


urlpatterns = [
    url(r'^list/$', TodoListView.as_view()),
]