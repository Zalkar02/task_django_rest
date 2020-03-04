from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tag.models import Tag, Task

class TagTests(APITestCase):
    def setUp(self):
        Tag.objects.create(name='Django')
        Tag.objects.create(name='Django rest')
        Task.objects.create(name='Django rest', description='Text')

    def test_create_tag(self):
        url = reverse('tag:create')
        data = {'name': 'DabTags',
                'tasks': [1]}
        response = self.client.post(url, data, format='json')
        tag = Tag.objects.get(name='DabTags')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tag.name, 'DabTags')
        self.assertEqual(len(tag.tasks.all()), 1)

    def test_list_tag(self):
        url = reverse('tag:list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(Tag.objects.all()))

    def test_detail_tag(self):
        tag = Tag.objects.get(name='Django rest')
        url = reverse('tag:detail', kwargs={'pk': tag.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], tag.name)
        self.assertEqual(response.data['tasks'], list(tag.tasks.all()))

    def test_put_tag(self):
        url = reverse('tag:detail', kwargs={'pk': 1})
        data = {'name': 'lOl',
                'tasks': [1]}
        response = self.client.post(url, data, format='json')
        tag = Tag.objects.get(name='lOl')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tag.name, 'lOl')
        self.assertEqual(len(tag.tasks.all()), 1)

    def test_delete_task(self):
        url = reverse('tag:detail', kwargs={'pk': 2})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)