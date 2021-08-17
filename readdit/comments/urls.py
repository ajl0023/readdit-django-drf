from django.conf.urls import url
from django.urls import include, path
from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from rest_framework import routers, views
from comments import views
from userAuth.views import UserView, LoginView
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.NewComment.as_view()),




]
