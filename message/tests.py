import os
import sys

from message_app.settings import BASE_DIR

IS_TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'
if IS_TESTING:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Message, Chat_room


class SendMessageAPITest(APITestCase):


    def test_send_message_success(self):
        """Test that a valid message is created successfully"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Message sent successfully')

        # Check that the message is stored in the database
        self.assertEqual(Message.objects.count(), 1)
        message = Message.objects.first()
        self.assertEqual(message.sender, self.sender)
        self.assertIn(self.receiver1, message.receiver.all())
        self.assertIn(self.receiver2, message.receiver.all())
        self.assertEqual(message.content, "Hello everyone!")
        self.assertEqual(message.chat_room, self.chat_room)

    def test_send_message_invalid(self):
        """Test that invalid data returns 400"""
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('content', response.data)

