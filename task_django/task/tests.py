from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models import Task

class TaskTests(APITestCase):
    def setUp(self):
        Task.objects.create(name='Django', description='Text')
        Task.objects.create(name='Django rest', description='Text')

    def test_create_task(self):
        url = reverse('task:create')
        data = {'name': 'DabApps',
                'description': 'Text',
                'tags': []}
        response = self.client.post(url, data, format='json')
        task = Task.objects.get(name='DabApps')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(task.name, 'DabApps')
        self.assertEqual(task.description, 'Text')
        self.assertEqual(len(task.tags.all()), 0)

    def test_list_task(self):
        url = reverse('task:list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Task.objects.all()))

    def test_detail_task(self):
        task = Task.objects.get(name='Django rest')
        url = reverse('task:detail', kwargs={'pk': task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], task.name)
        self.assertEqual(response.data['description'], task.description)
        self.assertEqual(response.data['tags'], list(task.tags.all()))

    def test_put_task(self):
        url = reverse('task:detail', kwargs={'pk': 1})
        data = {'name': 'DabApps',
                'description': 'Text',
                'tags': []}
        response = self.client.put(url, data, format='json')
        task = Task.objects.get(name='DabApps')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(task.name, 'DabApps')
        self.assertEqual(task.description, 'Text')
        self.assertEqual(len(task.tags.all()), 0)

    def test_delete_task(self):
        url = reverse('task:detail', kwargs={'pk': 1})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)