from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    print (queryset)
    serializer_class = PostSerializer
