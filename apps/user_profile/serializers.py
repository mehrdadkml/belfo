
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from allauth.account.models import EmailAddress



UserModel = get_user_model()
