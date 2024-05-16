"""
Django settings for pipeline_sdk_use project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from celery import Celery
from pipeline.celery.queues import ScalableQueues  # noqa
from pipeline.celery.settings import *  # noqa
from pipeline.eri.celery import queues, step

CELERY_QUEUES.extend(queues.CELERY_QUEUES)  # noqa
CELERY_QUEUES.extend(queues.QueueResolver("api").queues())  # noqa

step.PromServerStep.port = 8002
app = Celery("proj")
app.config_from_object("django.conf:settings")
app.steps["worker"].add(step.PromServerStep)

# ScalableQueues.add(name='custom_queue_1')
# ScalableQueues.add(name='custom_queue_2')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "secret_keysecret_keysecret_keysecret_keysecret_key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pipeline",
    "pipeline.log",
    "pipeline.engine",
    "pipeline.contrib.node_timer_event",
    "pipeline.component_framework",
    "pipeline.variable_framework",
    "pipeline.django_signal_valve",
    "pipeline.contrib.periodic_task",
    "pipeline.contrib.node_timeout",
    "pipeline.contrib.rollback",
    "pipeline.contrib.plugin_execute",
    "django_celery_beat",
    "pipeline_test_use",
    "variable_app",
    "pipeline.eri",
    "eri_chaos",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

REDIS = {
    "host": os.getenv("PIPELINE_TEST_REDIS_HOST", "localhost"),
    "port": int(os.getenv("PIPELINE_TEST_REDIS_PORT") or 6379),
    "password": os.getenv("PIPELINE_TEST_REDIS_PASSWORD"),
    "db": int(os.getenv("PIPELINE_TEST_REDIS_DB") or 0),
}

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

WSGI_APPLICATION = "pipeline_sdk_use.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DB_TYPE = os.getenv("PIPELINE_TEST_DB_TYPE", "sqllite")

if DB_TYPE == "sqllite":
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.path.join(BASE_DIR, "db.sqlite3")}}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("PIPELINE_TEST_DB_NAME"),
            "USER": os.getenv("PIPELINE_TEST_DB_USER"),
            "PASSWORD": os.getenv("PIPELINE_TEST_DB_PWD"),
            "HOST": os.getenv("PIPELINE_TEST_DB_HOST", "localhost"),
            "PORT": int(os.getenv("PIPELINE_TEST_DB_PORT", 3306)),
            "TEST": {"CHARSET": "utf8", "COLLATION": "utf8_general_ci"},
        }
    }
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s %(message)s"}},
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler"},
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple"},
        # "pipeline_eri": {"level": "DEBUG", "class": "pipeline.eri.log.ERINodeLogHandler", "formatter": "simple"},
        "pipeline_eri": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple"},
    },
    "loggers": {
        "django.server": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "pipeline.eri.log": {"handlers": ["pipeline_eri"], "level": "DEBUG", "propagate": True},
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"

ENABLE_EXAMPLE_COMPONENTS = True

BROKER_VHOST = "/"

BROKER_URL = os.getenv("PIPELINE_TEST_BROKER_URL", "amqp://guest:guest@localhost:5672//")

# BROKER_URL = "redis://localhost:6379/0"

PIPELINE_DATA_BACKEND = "pipeline.engine.core.data.redis_backend.RedisDataBackend"

PIPELINE_DATA_CANDIDATE_BACKEND = "pipeline.engine.core.data.mysql_backend.MySQLDataBackend"

PIPELINE_DATA_BACKEND_AUTO_EXPIRE = True

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# ENGINE_ZOMBIE_PROCESS_DOCTORS = [
#     {
#         'class': 'pipeline.engine.health.zombie.doctors.RunningNodeZombieDoctor',
#         'config': {
#             'max_stuck_time': 30
#         }
#     }
# ]


PLUGIN_EXECUTE_QUEUE = "default"
