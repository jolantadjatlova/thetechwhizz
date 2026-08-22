import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-cw&0#spu96x4#u8ykev#=w=g(r^m&z#l7d^z#oszyndu(se(qi"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# Email: print to console by default so nothing is actually sent while
# developing. If a SendGrid API key is set locally, use real SendGrid
# sending instead, so the full flow can be tested before deploying.
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "")
DEFAULT_FROM_EMAIL = "info@thetechwhizz.co.uk"

if SENDGRID_API_KEY:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass