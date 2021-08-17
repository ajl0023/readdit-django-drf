from comments.serializers import CommentSerializer
from rest_framework.fields import SerializerMethodField
from posts.models import Posts
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    voteState = SerializerMethodField()
    voteTotal = SerializerMethodField()
    author = serializers.SlugRelatedField(

        read_only=True,
        slug_field='username'
    )

    class Meta:

        fields = ['content', 'title', 'author', 'voteState', 'voteTotal', 'id']
        model = Posts

    def get_voteState(self, obj):

        return obj.voteState

    def get_voteTotal(self, obj):

        return obj.voteTotal


class SinglePostSerializer(serializers.ModelSerializer):
    voteState = serializers.IntegerField()
    voteTotal = SerializerMethodField()
    comments = SerializerMethodField()

    author = serializers.SlugRelatedField(

        read_only=True,
        slug_field='username'
    )

    class Meta:

        fields = ['content', 'title', 'author',
                  'voteState', 'voteTotal', 'id', 'comments']
        model = Posts

    def get_voteState(self, obj):

        return obj.voteState

    def get_voteTotal(self, obj):

        return obj.voteTotal

    def get_comments(self, obj):
        print(obj.comments.all(),123123123)
        return CommentSerializer(obj.comments.all(), many=True).data
