import os
import datetime
from pathlib import Path
import socket 
from decouple import config
from unipath import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=config('SECRET_KEY', default = os.environ.get("DJANGO_SECRET_KEY", "54g6s%qjfnhbpw0zeoei=$!her*y(p%!&84rs$4l85io"))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=config('DEBUG', default=True, cast=bool)

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["10.0.2.2", "host.docker.internal", "api.prodxcloud.io"]
    
# ALLOWED_HOSTS = [os.getenv("ALLOWED_PORTS")]
ALLOWED_HOSTS=['*']
# APPEND_SLASH = False
# Cors Settings
BACKEND_DOMAIN='http://api.prodxcloud.io/'
PAYMENT_SUCCESS_URL='http://api.prodxcloud.io:8585/api/v1/products/success/'
PAYMENT_CANCEL_URL='http://api.prodxcloud.io:8585/api/v1/products/cancel/'
CORS_ORIGIN_ALLOW_ALL=True

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
    "https://prodxcloud.io",
    "https://api.prodxcloud.io",
    "http://52.90.4.135",
    "http://52.90.4.135:8585",
    "http://127.0.0.1:8000"
]

CORS_ALLOW_CREDENTIALS=True
# CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS')

# Django data browser
# References : https://pypi.org/project/django-data-browser/
# DATA_BROWSER_FE_DSN="https://af64f22b81994a0e93b82a32add8cb2b@o390136.ingest.sentry.io/5231151"

# Application definition # # # # #
INSTALLED_APPS = [
    # 'django_tenants',
    # 'apps.app',  
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    "corsheaders",
    'django_filters',
    'drf_yasg',
    'widget_tweaks',
    'apps.home',
    'apps.snippets',
    'apps.users',
    'apps.finances',
    'apps.payments',
    'apps.products',
    'django_ledger'

]



# # Multi-tenant settings Application definition # # # # #
TENANT_APPS = ["client_app"]
# INSTALLED_APPS = SHARED_APPS + [app for app in TENANT_APPS if app not in SHARED_APPS]
# TENANT_APPS = ["apps.home"]
# TENANT_MODEL = "app.Client"
# TENANT_DOMAIN_MODEL = "app.Domain"
# PUBLIC_SCHEMA_URLCONF = "app.urls"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "django_tenants.middleware.main.TenantMainMiddleware"
]

# DEBUG_TOOLBAR_PANELS = [
#         'debug_toolbar.panels.versions.VersionsPanel',
#         'debug_toolbar.panels.settings.SettingsPanel',
#         'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#         'debug_toolbar.panels.timer.TimerPanel',
#         'debug_toolbar.panels.headers.HeadersPanel',
#         'debug_toolbar.panels.request.RequestPanel',
#         'debug_toolbar.panels.sql.SQLPanel',
#         'debug_toolbar.panels.cache.CachePanel',
#         'debug_toolbar.panels.profiling.ProfilingPanel',
#         'debug_toolbar.panels.history.HistoryPanel',
#         'template_timings_panel.panels.TemplateTimings.TemplateTimings',
#     ]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    "host.docker.internal",
    "api.prodxcloud.io"
]

ROOT_URLCONF = 'multitenantsaas.urls'
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'multitenantsaas.wsgi.application'

#Connect to Neo4j Database
# config.DATABASE_URL = 'bolt://neo4j+s://f89c638e.databases.neo4j.io:7687'

# SQLite Database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

## Postgres Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get("POSTGRES_NAME"),
#         'USER': os.environ.get("POSTGRES_USER"),
#         'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
#         'HOST': os.environ.get("POSTGRES_HOST"),
#         'PORT': int(os.environ.get("POSTGRES_PORT")),
#     }
# }

# DATABASE_ROUTERS = (
#     'django_tenants.routers.TenantSyncRouter',
# )


# Password validation 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# JWT Authentification parameters
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

REST_FRAMEWORK = {

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 20,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework_simplejwt.authentication.JWTAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    # ), 
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_PROFILE_MODULE = 'users.MyUser'
# AUTH_USER_MODEL = 'users.MyUser'

# Internationalization #
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# Extra places for collectstatic to find static files. #
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


# Caching parameters
# MEMUSAGE_ENABLED = True
# MEMUSAGE_LIMIT_MB = 2048
# C_FORCE_ROOT = 'true' 
# C_FORCE_ROOT = True

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': os.environ.get("BROKER_URL", "redis://redis:6379/1"),
#         "KEY_PREFIX": "DB2",
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }


#Celery parameters and Redis  Production parameters
# CELERY_BROKER_URL=os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
# CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
# CELERY_BROKER_TRANSPORT_URL=os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0")
# # CELERY_RESULT_BACKEND= os.environ.get("CELERY_RESULT_BACKEND", "db+postgresql://postgres:postgres@api.prodxcloud.io/DB2") 
# BROKER_URL=os.environ.get("BROKER_URL", "redis://redis:6379/1")
# CELERY_ACCEPT_CONTENT=['application/json']
# CELERY_TASK_SERIALIZER='json'
# CELERY_RESULT_SERIALIZER='json'
# CELERY_TIMEZONE="Asia/Singapore"
# CELERY_TASK_TRACK_STARTED=True
# CELERY_TASK_TIME_LIMIT=30 * 60
# CELERY_TASK_ALWAYS_EAGER=True
# CELERY_TASK_EAGER_PROPAGATES=True
# CELERY_ALWAYS_EAGER=True
# BROKER_HEARTBEAT= 10 
# BROKER_HEARTBEAT_CHECKRATE =2.0
# BROKER_POOL_LIMIT=None
# BROKER_CONNECTION_RETRY=False
# BROKER_CONNECTION_MAX_RETRIES=0
# BROKER_CONNECTION_TIMEOUT=120
# BROKER_CONNECTION_RETRY_ON_STARTUP=True
# BROKER_CHANNEL_ERROR_RETRY=True
# BROKER_TRANSPORT="kombu.transport.django"

#Parameters for SMTP EMAIL EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'  # Your SES region endpoint
EMAIL_PORT = 587  # Use 465 for SSL/TLS if preferred
EMAIL_USE_TLS = True  # Set to False if using SSL (port 465)
EMAIL_HOST_USER = ''  # SMTP username from AWS SES
EMAIL_HOST_PASSWORD = ''  # SMTP password from AWS SES
DEFAULT_FROM_EMAIL = ''  # Use your verified domain email

