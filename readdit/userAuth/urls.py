from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userAuth import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('login', views.LoginView.as_view()),
    
    


]
urlpatterns = format_suffix_patterns(urlpatterns)
