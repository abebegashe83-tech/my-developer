
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


# --------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    if not DEBUG:
        raise ImproperlyConfigured(
            "DJANGO_SECRET_KEY must be set when DEBUG is False."
        )
    SECRET_KEY = "dev-secret-key-change-me"


# --------------------------------------------------
# FRONTEND CONFIGURATION
# --------------------------------------------------

DEFAULT_FRONTEND_URL = "https://my-developer-w91p.vercel.app"
FRONTEND_URL = os.getenv("FRONTEND_URL", DEFAULT_FRONTEND_URL).rstrip("/")


# --------------------------------------------------
# ALLOWED HOSTS
# --------------------------------------------------

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "my-developer.onrender.com,localhost,127.0.0.1,[::1]",
    ).split(",")
    if host.strip()
]


# --------------------------------------------------
# INSTALLED APPLICATIONS
# --------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "portfolio",
]


# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------------------------------------
# URL AND WSGI CONFIGURATION
# --------------------------------------------------

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# --------------------------------------------------
# TEMPLATES
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# --------------------------------------------------
# DATABASE
# --------------------------------------------------
# This preserves your existing SQLite configuration.
# Remember that SQLite data on an ephemeral Render
# filesystem may not persist across deployments.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# --------------------------------------------------
# STATIC FILES
# --------------------------------------------------

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --------------------------------------------------
# CORS CONFIGURATION
# --------------------------------------------------
# Allow your deployed Vercel frontend to call Django.

CORS_ALLOWED_ORIGINS = [
    origin.strip().rstrip("/")
    for origin in os.getenv(
        "CORS_ALLOWED_ORIGINS",
        "https://my-developer-w91p.vercel.app",
    ).split(",")
    if origin.strip()
]

CORS_ALLOW_ALL_ORIGINS = DEBUG


# --------------------------------------------------
# CSRF CONFIGURATION
# --------------------------------------------------

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CSRF_TRUSTED_ORIGINS",
        "https://my-developer-w91p.vercel.app",
    ).split(",")
    if origin.strip()
]


# --------------------------------------------------
# RENDER HTTPS CONFIGURATION
# --------------------------------------------------

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG


# --------------------------------------------------
# EMAIL CONFIGURATION
# --------------------------------------------------

EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend",
)

if (
    EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend"
    and not (
        os.getenv("EMAIL_HOST")
        and os.getenv("EMAIL_HOST_USER")
        and os.getenv("EMAIL_HOST_PASSWORD")
    )
):
    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
        if DEBUG
        else "django.core.mail.backends.smtp.EmailBackend"
    )

EMAIL_HOST = os.getenv("EMAIL_HOST", "")

EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))

EMAIL_USE_TLS = (
    os.getenv("EMAIL_USE_TLS", "False").lower() == "true"
)

EMAIL_USE_SSL = (
    os.getenv("EMAIL_USE_SSL", "False").lower() == "true"
)

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    "noreply@example.com",
)

EMAIL_TO = os.getenv(
    "EMAIL_TO",
    "abebegashe83@gmail.com",
)

SERVER_EMAIL = DEFAULT_FROM_EMAIL
