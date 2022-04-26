from rest_framework import serializers
from api.models import Article
from api.models import Comment

from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'owner', 'comments']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments']


class FinalLevelRepliesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'owner', 'article', 'parent']

class FirstLevelRepliesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reply_set = FinalLevelRepliesSerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'text', 'owner', 'article', 'parent', 'reply_set']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    reply_set = FirstLevelRepliesSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'owner', 'article', 'parent', 'reply_set']
