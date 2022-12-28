from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.models import User
from django.utils.timezone import timedelta, now
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

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

class MessageViewSet(ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

	def create(self, request, *args, **kwargs):
		try:
			instance = Message.objects.get(
				id = super().create(self, request, *args, **kwargs).data.get('id'))
			# instance.text = self.request.
			instance.user.pk = self.request.user.pk
			instance.save()
			return Response(
				status = HTTP_201_CREATED,
				data = MessageSerial(instance=instance, many=False)
			)
		except:
			return Response(
				status = HTTP_400_BAD_REQUEST,
				data = {"ERR: Bad Request"}
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
				status = HTTP_400_BAD_REQUEST,
				data = {"ERR: Bad Request"}
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
				status = HTTP_400_BAD_REQUEST,
				data = {"ERR: Bad Request"}
			)

class HTMXMessageView(APIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerial
	permission_classes = [IsAuthenticated]

	def get(self, request, *args, **kwargs):
		if self.request.GET.get('id'):
			instance = Message.objects.get(id=self.request.GET.get('id'))
		else:
			instance = Message.objects.filter(created_at__gte=now() - timedelta(days=1))
		serial = MessageSerial( instance, many = True )
		return Response(
			status = HTTP_200_OK,
			data = serial,
		)

	# def put(self, request, *args, **kwargs):
	# 	return Response()

	# def post(self, request, *args, **kwargs):
	# 	return Response()

	# def patch(self, request, *args, **kwargs):
	# 	return Response()

	# def delete(self, request, *args, **kwargs):
	# 	return Response()
