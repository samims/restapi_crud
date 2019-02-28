from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=30, null=True)
    content = models.TextField(blank=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


