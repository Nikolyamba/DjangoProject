from rest_framework import generics
from .models import Task
from .serializers import TaskCreateSerializer, TaskReadSerializer
from .tasks import sum_numbers, reverse_text, delayed

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        task = serializer.save()

        if task.type == "sum":
            job = sum_numbers.delay(task.payload)
        elif task.type == "reverse":
            job = reverse_text.delay(task.payload)
        elif task.type == "delayed":
            job = delayed.delay(task.payload)
        else:
            task.status = "error"
            task.result = {"error": "unknown task type"}
            task.save()
            return

        task.status = "pending"
        task.result = {"celery_id": job.id}
        task.save()

class TaskGetView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadSerializer
