from django.urls import path, include
from rest_framework import routers
from .views import ChatMessageViewSet

router = routers.DefaultRouter()
router.register(r'chatmessages', ChatMessageViewSet)

urlpatterns = [
  path('', include(router.urls), name='index'),
]