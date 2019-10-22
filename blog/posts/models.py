import uuid
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    updated_date = models.DateTimeField('date updated')
    published_date = models.DateTimeField('date published')
    content = models.TextField()
    title = models.CharField(max_length=150)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)