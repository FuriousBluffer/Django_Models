from django.urls import path, include
from trello_app import views

urlpatterns = [
    path('', views.index),
    path('add_task_list', views.add_task_list, name='add_task_list'),
    path('add_task_list_2', views.add_task_list_2, name='add_task_list_2'),
    path('add_task', views.add_task, name='add_task')
]

