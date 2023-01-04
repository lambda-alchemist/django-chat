from django.contrib import admin
from django.urls import path, re_path, include

from chat.urls import schema_view

urlpatterns = [
	path('rest/chat/', include('chat.urls')),
	path('rest/auth/', include('dj_rest_auth.urls')),
	path('rest/auth/signup/', include('dj_rest_auth.registration.urls')),
]

urlpatterns += [
	path('admin/', admin.site.urls),
	path('rest/', include('rest_framework.urls')),
	re_path(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0)),
	re_path(r'^swagger$', schema_view.with_ui('swagger', cache_timeout=0)),
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0)),
]
