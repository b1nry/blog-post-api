from posts.models import Post 
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'id', 'title', 'content', 'published_date', 'updated_date')