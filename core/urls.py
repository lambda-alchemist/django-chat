from django.urls import path, re_path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter

from chat.views import (
	TestPage, LandingPage,
	IndexPage, LoginPage,
	SignupPage, LogoutPage,
	get_user, get_latest_user, check_user,
	# get_message, get_lastest_messages,
)

schema_view = get_schema_view(
	info = Info(
		title="Django Open Chat API",
		default_version="v1",
		description="An open public chat, written in PyDj",
		contact=Contact(email="alchemist.software@proton.me"),
		license=License(name="MIT License"),
	),
	public = True,
	permission_classes = [IsAuthenticatedOrReadOnly]
)

urlpatterns = [
	path('auth/', include('dj_rest_auth.urls'), name='base-auth'),
	path('auth/signup/', include('dj_rest_auth.registration.urls'), name='base-auth-signup')
]

urlpatterns += [
	path('chat/', LandingPage.as_view(), name='page-landing'),
	path('chat/test/', TestPage.as_view(), name='page-test'),
	path('chat/index/', IndexPage.as_view(), name='page-index'),
	path('chat/login/', LoginPage.as_view(), name='page-login'),
	path('chat/logout/', LogoutPage.as_view(), name='page-logout'),
	path('chat/singup/', SignupPage.as_view(), name='page-signup'),
]

urlpatterns += [
	path(r'^hx/check-user$', check_user, name='user-check'),
	path(r'^hx/get-user/<int:pk>$', get_user, name='get-user-id'),
	path(r'^hx/get-user-recent$', get_latest_user, name='get-user-recent'),
	# path('hx/get-message/<int:pk>', get_message, name='get-message-id'),
	# path('hx/get-message-latest/', get_latest_messages, name='get-message-recent'),
]

urlpatterns += [
	path('admin/', admin.site.urls),
	re_path(r'^drf/', include('rest_framework.urls'), name='schema-session'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
