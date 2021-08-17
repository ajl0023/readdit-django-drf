from .serializers import UserSerializer
from posts.serializers import SinglePostSerializer
from posts.utils import getVoteState
from posts import views
from django.shortcuts import render
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from posts.serializers import PostSerializer
from posts.models import Posts
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.expressions import Case, F, OuterRef, Subquery, Value, When, Window
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.db.models.functions import Coalesce
import json
import datetime
from rest_framework.authtoken.models import Token
from django.contrib.messages import get_messages
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class LoginView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def post(self, request, format=None):

        storage = get_messages(request)
        print(storage)
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        token = Token.objects.create(user=user)

        if user is not None:
            response = Response()
            max_age = 365 * 24 * 60 * 60

            expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)

            # response.set_cookie(
            #     key='TOKEN',
            #     value=token.key,

            #     expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S UTC"),
            #     max_age=max_age,

            # )
            response.data = {
                "user": user.id,
                "token": token.key

            }

            return response

        else:

            return Response('error')


class UserView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        print(user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
