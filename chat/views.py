from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from chat.models import Message
from chat.serial import MessageSerial
from chat.forms import RegisterForm

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('')

class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('')

# class HTMXMessage(APIView):
# 	queryset = Message.objects.all()
# 	serializer_class = MessageSerial
# 	permission_classes = [IsAuthenticatedOrReadOnly]
# 	def get(self, request, *args, **kwargs):
# 		return

class IndexPage(TemplateView):
	template_name = 'index.html'

class LoginPage(LoginView):
	template_name = 'login.html'

class Logoutpage(LogoutView):
	pass

class SignupPage(FormView):
	template_name = 'signup.html'
	form_class = RegisterForm
	success_url = reverse_lazy('login-page')
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

def check_user(request):
	if get_user_model().objects.filter(username=request.POST.get('username')).exists():
		return HttpResponse("This username already exists")
	else:
		return HttpResponse("")

