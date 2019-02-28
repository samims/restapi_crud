from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'author'
        ]
        read_only_fields = ('author',)

    def get_author(self, obj):
        request = self.context['request']
        email = request.user.email
        return email

    def create(self, validated_data):
        email = self.get_author(self.instance)
        author = User.objects.get(email=email)
        validated_data["author"] = author
        post = Post.objects.create(**validated_data)
        return post
