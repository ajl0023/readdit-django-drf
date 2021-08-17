from posts.models import Comments
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class CommentSerializer(serializers.ModelSerializer):
    voteState = SerializerMethodField()

    class Meta:

        fields = ['content', 'author',
                  'id', 'voteState']
        model = Comments

    def get_voteState(self, obj):
        print(obj)
        return obj.voteState

    def get_voteTotal(self, obj):

        return obj.voteTotal
