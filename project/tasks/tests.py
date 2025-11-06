from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='ali', password='123456')
        self.task = Task.objects.create(user=self.user, title='Test task', completed=False)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test task')
        self.assertFalse(self.task.completed)

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='ali', password='123456')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {'title': 'API Task', 'completed': False})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'API Task')