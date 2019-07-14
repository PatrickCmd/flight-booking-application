import os


def get_env():
    if os.environ.get('APP_SETTINGS') == "production":
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbs.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbs.settings.development')
