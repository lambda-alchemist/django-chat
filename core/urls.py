from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter
from drf_yasg.openapi import Info, Contact, License
from drf_yasg.views import get_schema_view

from django.contrib import admin
from django.urls import path, re_path, include

from chat.views import (
	MessageView,
	ProfileView,
	GroupView,
	PostView,
	ReelView,
	ProfilePictureView,
	GroupPictureView,
	PostPictureView,
	ReelPictureView
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

router = DefaultRouter()
router.register('api/chat/message', MessageView)
router.register('api/chat/profile', ProfileView)
router.register('api/chat/group', GroupView)
router.register('api/chat/post', PostView)
router.register('api/chat/reel', ReelView)

urlpatterns = [
	path('', include(router.urls)),
	path('api/auth/', include('dj_rest_auth.urls')),
	path('api/auth/signup/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += [
	re_path(r'api/chat/profile/(?P<pk>\d+)/picture', ProfilePictureView.as_view(), name='profile-picture'),
	re_path(r'api/chat/group/(?P<pk>\d+)/picture', GroupPictureView.as_view(), name='group-picture'),
	re_path(r'api/chat/post/(?P<pk>\d+)/picture', PostPictureView.as_view(), name='post-picture'),
	re_path(r'api/chat/reel/(?P<pk>\d+)/picture', ReelPictureView.as_view(), name='reel-picture'),
]

urlpatterns += [
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^drf/', include('rest_framework.urls'), name='schema-session'),
	re_path(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	re_path(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
