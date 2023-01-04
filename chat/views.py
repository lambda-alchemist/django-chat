from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView, SocialLoginView

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
)
from django.urls import reverse_lazy

from chat.serial import (
	MessageSerial,
	ProfileSerial,
	GroupSerial,
	PostSerial,
	ReelSerial,
)
from chat.models import (
	Message,
	Profile,
	Group,
	Post,
	Reel,
)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')

class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')



class ProfileView(ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

class GroupView(ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

class MessageView(ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

	def create(self, request, *args, **kwargs):
		message = super().create(self, request, *args, **kwargs)
		instance = Message.objects.get(id = message.data.get('id'))
		instance.user.pk = self.request.user.pk
		instance.save()
		return Response(
			status = HTTP_201_CREATED,
			data = MessageSerial(instance=instance, many=False).data
		)

class ReelView(ModelViewSet):
	queryset = Reel.objects.all()
	serializer_class = ReelSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

class PostView(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerial
	permission_classes = [IsAuthenticatedOrReadOnly]

