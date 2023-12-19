from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An exelent subtitle",
            author="Tom",
            isbn="123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "An exelent subtitle")
        self.assertEqual(self.book.author, "Tom")
        self.assertEqual(self.book.isbn, "123")

    def test_book_listview(self):
        response = self.client.get(reverse("n_home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "An exelent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
