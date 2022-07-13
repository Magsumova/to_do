from asyncio import Task
from django.contrib import admin
from django.urls import path, include

from to_do_app.views import TaskApiView

urlpatterns = [
    path('api/tasks', TaskApiView.as_view()),
]