from rest_framework import generics as g

from .models import Task
from .serializer import TaskSerializer


class TaskList(g.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreate(g.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(g.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer