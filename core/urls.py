from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from chat.views import ChatViewSet
# from page.views import PageViewSet

schema_view = get_schema_view(
	openapi.Info(
		title="Snippets API",
		default_version="v1",
		description="Django Open Chat API",
		contact=openapi.Contact(email="alchemist.software@proton.me"),
		license=openapi.License(name="MIT License"),
	),
	public = True,
	permission_classes=[permissions.IsAuthenticatedOrReadOnly]
)

router = routers.DefaultRouter()
# router.register(r'chat', ChatViewSet)
# router.register(r'page', PageViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('admin/', admin.site.urls),
	path('dj-auth/', include('dj_rest_auth.urls')),
	path('dj-auth/registration/', include('dj_rest_auth.registration.urls')),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
