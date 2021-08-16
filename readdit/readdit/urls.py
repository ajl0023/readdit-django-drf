from django.urls import include, path
from rest_framework import routers
from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostList, basename='posts')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('posts/', include('posts.urls')),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
