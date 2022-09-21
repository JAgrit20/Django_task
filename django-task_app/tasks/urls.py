#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [

    path('', views.TaskListView.as_view(), name='task_list'),

]