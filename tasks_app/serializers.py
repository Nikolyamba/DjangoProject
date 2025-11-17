from rest_framework import serializers

from tasks_app.models import Task

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "type", "payload")
        read_only_fields = ("id",)

class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'