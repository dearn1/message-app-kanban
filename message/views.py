from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from message.models import Message
from message.serializers import MessageSerializer


@api_view(['POST'])
def send_message(request):
    message_serializer = MessageSerializer(data=request.data)
    if message_serializer.is_valid():
        message_serializer.save()
        return Response({"message": 'Message sent successfully'},
                        status=status.HTTP_201_CREATED)
    else:
        return Response(message_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
