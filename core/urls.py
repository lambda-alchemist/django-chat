from django.urls import path, re_path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter

from chat.views import MessageViewSet
# from page.views import PageViewSet

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
router.register('chat', MessageViewSet, 'chat-messages')
# router.register('page', PageViewSet, 'page')


urlpatterns = [
	path('', include(router.urls)),
	path('admin/', admin.site.urls),
	path('auth/', include('dj_rest_auth.urls')),
	path('auth/signup/', include('dj_rest_auth.registration.urls')),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
