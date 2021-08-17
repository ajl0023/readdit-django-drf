from django.views.generic.base import TemplateResponseMixin
from posts.serializers import SinglePostSerializer
from posts.utils import getVoteState
from posts import views
from django.shortcuts import render

# Create your views here.
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


class TemplateView(TemplateResponseMixin):
    def get(self, request, id, format=None):
        return render(request, "build/index.html")
    """
    API endpoint that allows users to be viewed or edited.
    """
