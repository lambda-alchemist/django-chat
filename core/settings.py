from pathlib import Path
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', ['localhost', '127.0.0.1', '::1'])
SECRET_KEY = str(environ.get('SECRET_KEY'))
DEBUG = environ.get('DEBUG', 1)

INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"django.contrib.sites",

	"rest_framework",
	"rest_framework.authtoken",
	"rest_framework_simplejwt",
	"drf_yasg",
	"dj_rest_auth",
	"dj_rest_auth.registration",
	"allauth",
	"allauth.account",
	"allauth.socialaccount",
	"allauth.socialaccount.providers.github",
	"django_extensions",

	"chat",
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
	"django_htmx.middleware.HtmxMiddleware",
]

REST_FRAMEWORK = {
	# 'DEFAULT_PERMISSION_CLASSES': [
	# 	'rest_framework.permissions.IsAuthenticatedOrReadOnly',
	# 	'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
	# ],
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
	),
	'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema'
}
AUTH_USER_MODEL = 'chat.User'
REST_SESSION_LOGIN = True
JWT_AUTH_COOOKIE = 'auth'
REST_USE_JWT = True

SITE_ID = 1
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_REQUIRED = False

SWAGGER_SETTINGS = {
	'LOGIN_URL': 'drf/login',
	'LOGOUT_URL': 'drf/logout',
}

ROOT_URLCONF = "core.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.template.context_processors.debug",
				"django.template.context_processors.request",
				"django.contrib.auth.context_processors.auth",
				"django.contrib.messages.context_processors.messages",
			],
		},
	},
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": BASE_DIR / "db.sqlite3",
	}
}

AUTH_PASSWORD_VALIDATORS = [
	{"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
	{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
	{"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
	{"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
