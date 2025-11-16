from django.urls import path
from .views import TaskCreateView, TaskGetView

urlpatterns = [
    path('tasks/', TaskCreateView.as_view()),
    path('tasks/<uuid:pk>/', TaskGetView.as_view()),
]