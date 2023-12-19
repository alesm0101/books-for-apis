from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model: Book
    template_name: "book_list.html"

    # required ??
    def get_queryset(self):
        return Book.objects.order_by("id")
