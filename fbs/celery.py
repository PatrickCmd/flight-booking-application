import os

from celery import Celery
from django.conf import settings

if os.environ["APP_SETTINGS"] == "development":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbs.settings.development")

if os.environ["APP_SETTINGS"] == "production":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fbs.settings.production")

app = Celery("fbs")

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)
