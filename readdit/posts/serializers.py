from posts.models import Posts
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    print(Posts._meta.fields)

    class Meta:

        fields = '__all__'
        model = Posts
