from rest_framework import serializers
from board.models import Post, Board
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    viewer_num = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['url', 'id', 'created', 'author', 'board', 'title', 'content', 'viewer_num']


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = Board
        fields = ['url', 'id', 'name', 'posts']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']
