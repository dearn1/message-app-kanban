from django.urls import path, include
from rest_framework.routers import DefaultRouter

from message.viewsets import Chat_roomViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'chat_rooms', Chat_roomViewSet, basename='chat_rooms')
router.register(r'message', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]