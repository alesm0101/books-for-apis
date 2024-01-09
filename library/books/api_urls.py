### N

from django.urls import path

from .api_views import BookApiView

urlpatterns = [path("", BookApiView.as_view(), name="api_book_list")]
