from django.shortcuts import render
from rest_framework import viewsets, generics

from tasks_app.models import Task
from tasks_app.serializers import TaskCreateSerializer, TaskReadSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

class TaskGetView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadSerializer
