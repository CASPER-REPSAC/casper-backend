from rest_framework import serializers
from board.models import Post, Category, Suggestion, Chat


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'posts']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    viewer_num = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['url', 'id', 'author', 'created_date', 'viewer_num', 'category', 'title', 'content']


class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    chats = serializers.HyperlinkedRelatedField(many=True, view_name='chat-detail', read_only=True)

    class Meta:
        model = Suggestion
        fields = ['url', 'id', 'author', 'created_date', 'type', 'title', 'content', 'chats']


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Chat
        fields = ['url', 'id', 'author', 'suggestion', 'created_date', 'content']
