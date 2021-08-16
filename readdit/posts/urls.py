from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.PostList.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
