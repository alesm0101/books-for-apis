from django.test import TestCase

# Create your tests here.

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(title="First Todo", body="A body text here")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body text here")
        # for __str__
        self.assertEqual(str(self.todo), "First Todo")
