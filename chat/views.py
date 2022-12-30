from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
)
from django.utils.timezone import now, timedelta
from django.urls import reverse_lazy

from chat.models import Message, Group, User
from chat.serial import MessageSerial, GroupSerial

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')

class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')

class MessageView(ModelViewSet):
	queryset = Message.objects.filter()
	serializer_class = MessageSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

	def create(self, request, *args, **kwargs):
		try:
			msg = super().create(self, request, *args, **kwargs)
			instance = Message.objects.get(id = msg.data.get('id'))
			instance.sender.pk = self.request.user.pk
			instance.save()
			return Response(
				status = HTTP_201_CREATED,
				data = MessageSerial(instance=instance, many=False)
			)
		except:
			return Response(
				status = HTTP_500_INTERNAL_SERVER_ERROR,
				data = {"ERR: 500"}
			)

	def retrive(self, request, *args, **kwargs):
		try:
			msg = super().retrieve(request, *args, **kwargs)
			instance = Message.objects.get(id=msg.data.get('id'))
			return Response(
				status = HTTP_200_OK,
				data = MessageSerial(instance=instance, many=False)
			)
		except:
			return Response(
				status = HTTP_500_INTERNAL_SERVER_ERROR,
				data = {"ERR: 500"}
			)

	def list(self, request, *args, **kwargs):
		try:
			instance = Message.objects.filter(created_at__gt=now() - timedelta(days=1))
			return Response(
				status = HTTP_200_OK,
				data = MessageSerial(instance, many=True).data
			)
		except:
			return Response(
				status = HTTP_500_INTERNAL_SERVER_ERROR,
				data = {"ERR: Bad Request"}
			)

class GroupView(ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerial
	permission_classes = [IsAuthenticated]

