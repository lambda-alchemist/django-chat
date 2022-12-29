from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from django.utils.timezone import timedelta, now
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR
from django_htmx.http import HttpResponseStopPolling, HttpResponseClientRefresh

from chat.models import Message
from chat.serial import MessageSerial

callback_url = 'localhost:8000/auth/login'

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = callback_url
class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = callback_url

class HTMXMessage(APIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

	def get(self, request, *args, **kwargs):
		try:
			return Response()
		except:
			return Response(status = HTTP_500_INTERNAL_SERVER_ERROR, data = {'ERR: Something went wrong :/'})

	# def put(self, request, *args, **kwargs):
	# 	return Response()

	# def post(self, request, *args, **kwargs):
	# 	return Response()

	# def patch(self, request, *args, **kwargs):
	# 	return Response()

	# def delete(self, request, *args, **kwargs):
	# 	return Response()
