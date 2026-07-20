import os

import cloudinary

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

CSRF_TRUSTED_ORIGINS = [

    "https://thetechwhizz-a8e4bd1567a3.herokuapp.com",

]

# WhiteNoise handles static files.

STORAGES["staticfiles"]["BACKEND"] = (

    "whitenoise.storage.CompressedManifestStaticFilesStorage"

)

# Compatibility setting for django-cloudinary-storage's collectstatic command.

# Django itself uses STORAGES above.


# Cloudinary handles uploaded media files.

STORAGES["default"]["BACKEND"] = (

    "cloudinary_storage.storage.MediaCloudinaryStorage"

)

cloudinary.config(

    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),

    api_key=os.environ.get("CLOUDINARY_API_KEY"),

    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),

    secure=True,

)

LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "handlers": {

        "console": {

            "class": "logging.StreamHandler",

        },

    },

    "root": {

        "handlers": ["console"],

        "level": "WARNING",

    },

    "loggers": {

        "django": {

            "handlers": ["console"],

            "level": "ERROR",

            "propagate": False,

        },

    },

}

try:

    from .local import *

except ImportError:

    pass