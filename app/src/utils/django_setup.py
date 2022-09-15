import os

import django.conf
from django.core.wsgi import get_wsgi_application


django.conf.ENVIRONMENT_VARIABLE = 'dj'
os.environ.setdefault('dj', "BetBot.settings")
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

application = get_wsgi_application()
