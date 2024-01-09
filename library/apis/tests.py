from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from books.models import Book

from rest_framework import status
from rest_framework.test import APITestCase


class APITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An exelent subtitle",
            author="Tom",
            isbn="123",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"--->{Book.objects.first()}---")
        self.assertEqual(Book.objects.count(), 1)
        # self.assertContains(response, self.book)  # <-- doesn't work here
        # self.assertContains(response.data, Book.objects.first())
