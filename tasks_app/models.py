import uuid

from django.db import models

class Task(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    payload = models.JSONField()
    status = models.CharField(max_length=20, default="pending")
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

