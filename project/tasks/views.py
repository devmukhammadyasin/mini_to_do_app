from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def index(request):
    return render(request, 'tasks/index.html')