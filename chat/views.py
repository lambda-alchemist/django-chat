from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from chat.models import ChatMessage
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

# class MessageViewSet(ModelViewSet):
# 	queryset = ChatMessage.objects.all()
# 	serializer_class = MessageSerial

# 	def create(self, request, *args, **kwargs):
# 		try:
# 			msg = super().create(self, request, *args, **kwargs)
# 			instance = ChatMessage.objects.get()
# 			return Response(
# 				status = HTTP_201_CREATED,
# 				data = MessageSerial(instance=instance, many=False)
# 			)
# 		except:
# 			return Response(
# 				status = HTTP_400_BAD_REQUEST
# 				data = {"ERR: Bad Request"}
# 			)

