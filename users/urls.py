from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

app_name = 'users'

urlpatterns = [

] + router.urls
