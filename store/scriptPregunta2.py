# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adadis.settings")

# import django
# django.setup()

# from django.conf 
import settings

print(f"SESSION_COOKIE_AGE: {settings.SESSION_COOKIE_AGE}")
print(f"SESSION_COOKIE_DOMAIN: {settings.SESSION_COOKIE_DOMAIN}")
print(f"SESSION_COOKIE_SECURE: {settings.SESSION_COOKIE_SECURE}")
print(f"SESSION_EXPIRE_AT_BROWSER_CLOSE: {settings.SESSION_EXPIRE_AT_BROWSER_CLOSE}")
print(f"SESSION_SAVE_EVERY_REQUEST: {settings.SESSION_SAVE_EVERY_REQUEST}")

