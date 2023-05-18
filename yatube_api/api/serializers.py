from rest_framework import serializers
from .models import Post
from .models import Group
from .models import Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'all'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = 'all'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'all'
