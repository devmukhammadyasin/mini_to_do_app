from django.urls import path
from .views import TaskListCreateView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]