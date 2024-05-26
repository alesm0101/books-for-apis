from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions

from .models import Post
from .serlializers import PostSerializer
from .permissions import IsAuthorOrReadOnlyAuthenticated


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnlyAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
