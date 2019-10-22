from posts.models import Post 
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()
    id = serializers.UUIDField()
    published_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()

    class Meta:
        model = Post