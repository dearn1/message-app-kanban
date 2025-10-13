from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from message.models import Message


# Create your views here.

def send_message(request):
    sender = request.user
    receiver = request.data.get('receiver')
    content = request.data.get('content')
    chat_room = request.data.get('chat_room')
    message = Message.objects.create(sender=sender,
                                     receiver=receiver,
                                     content=content,
                                     chat_room=chat_room)
    return Response({'message': 'Message sent successfully'},
                    status=status.HTTP_201_CREATED)