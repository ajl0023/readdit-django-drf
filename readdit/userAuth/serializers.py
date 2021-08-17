from rest_framework.fields import SerializerMethodField
from posts.models import Posts
from posts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ['id', 'username']
        model = User
