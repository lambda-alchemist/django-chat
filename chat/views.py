from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.registration.views import SocialLoginView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.views.generic import FormView, TemplateView
from django.http.response import HttpResponse
from django.urls import reverse_lazy, reverse
from django.core import paginator
from django.conf import settings

from chat.forms import RegisterForm

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')

class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    callback_url = reverse_lazy('index')

class TestPage(TemplateView):
	template_name = 'pages/test.html'

class LandingPage(TemplateView):
	template_name = 'pages/landing.html'

class IndexPage(TemplateView):
	template_name = 'components/landing.html'

class LoginPage(LoginView):
	template_name = 'pages/login.html'

class LogoutPage(LogoutView):
	pass

class SignupPage(FormView):
	template_name = 'pages/signup.html'
	form_class = RegisterForm
	success_url = reverse_lazy('login-page')
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

html = ''

def check_user(request):
	if User.objects.filter(username=request.POST.get('username')).exists():
		return HttpResponse('Error: This username already exists')
	else:
		return HttpResponse('')

def get_user(request, html):
	if User.objects.filter(id = request.GET.get('id')).exists():
		html += ''
		return HttpResponse(html)
	else:
		html += 'Error: User not found'
		return HttpResponse(html)

def get_latest_user(request, html):
	users = User.objects.order_by('-date_joined')[:10]
	html += '<ul class="custom-user-list" >'
	for user in users:
		html += f'<li>{user.username} - {user.date_joined}</li>'
	html += '</ul>'
	return HttpResponse(html)

