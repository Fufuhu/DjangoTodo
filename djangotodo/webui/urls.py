from django.conf.urls import url
from webui.views.todo_view import TodoView,TodoListView


urlpatterns = [
    url(r'^list/$', TodoListView.as_view()),
    url(r'^$', TodoView.as_view()),
]