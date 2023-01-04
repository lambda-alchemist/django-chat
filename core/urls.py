from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, re_path, include

from chat.urls import schema_view

router = DefaultRouter()

urlpatterns = [
	path('', include(router.urls)),
	path('rest/chat/', include('chat.urls')),
	path('rest/auth/', include('dj_rest_auth.urls')),
	path('rest/auth/signup/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += [
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^rest/', include('rest_framework.urls'), name='schema-session'),
	re_path(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	re_path(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
