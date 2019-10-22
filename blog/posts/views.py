from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer