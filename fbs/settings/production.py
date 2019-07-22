import dj_database_url
import django_heroku

from .development import *  # noqa F403

django_heroku.settings(locals(), test_runner=False)
DATABASES = {"default": {}}
DATABASES["default"] = dj_database_url.config(
    default=os.environ.get("DATABASE_URL", None)  # noqa F405
)
