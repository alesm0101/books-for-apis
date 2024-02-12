from django.test import TestCase

# Create your tests here.

from .models import Todo


###
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="First Todo", body="A body text here")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body text here")
        # for __str__
        self.assertEqual(str(self.todo), "First Todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
