from django.conf.urls import url
from django.urls import include, path
from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from rest_framework import routers
import posts
from userAuth.views import UserView, LoginView
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('login', LoginView.as_view()),
    path('vote', posts.views.Vote.as_view()),
    path('me', UserView.as_view()),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),


    re_path(r"^$", TemplateView.as_view(template_name="index.html")),



]
print(url(r'^$', TemplateView.as_view(template_name="index.html")))
