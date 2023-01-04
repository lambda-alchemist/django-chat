from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.routers import DefaultRouter, SimpleRouter, BaseRouter
from drf_yasg.openapi import Info, Contact, License
from drf_yasg.views import get_schema_view

from django.urls import path, include

from chat.views import (
	MessageView,
	ProfileView,
	GroupView,
	PostView,
	ReelView,
)

schema_view = get_schema_view(
	info = Info(
		title = "Django Open Chat API",
		default_version = "v1",
		description = "An open public chat, written in PyDj",
		contact = Contact(email="alchemist.software@proton.me"),
		license = License(name="MIT License"),
	),
	public = True,
	permission_classes = [IsAuthenticatedOrReadOnly]
)

router = DefaultRouter()

router.register('message', MessageView)
router.register('profile', ProfileView)
router.register('group', GroupView)
router.register('post', PostView)
router.register('reel', ReelView)

urlpatterns = [path('', include(router.urls))]

