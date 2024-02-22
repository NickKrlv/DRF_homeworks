from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentViewSet, basename='payments')

app_name = 'users'

urlpatterns = [

] + router.urls
