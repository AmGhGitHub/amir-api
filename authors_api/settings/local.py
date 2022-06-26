from .base import *
import environ

env = environ.Env()
environ.Env.read_env()  # reading .env file

DEBUG = env.bool("DEBUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": env("DB_ENGINE"),
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_USER_PASSWORD"),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
