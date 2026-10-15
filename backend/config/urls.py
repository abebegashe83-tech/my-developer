
from ipaddress import ip_address
from urllib.parse import urlsplit

from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path


def api_home(request):
    frontend_url = settings.FRONTEND_URL
    if not settings.DEBUG:
        parsed_url = urlsplit(frontend_url)
        hostname = (parsed_url.hostname or "").lower()
        try:
            is_loopback = ip_address(hostname).is_loopback
        except ValueError:
            is_loopback = hostname == "localhost" or hostname.endswith(".localhost")

        if (
            parsed_url.scheme not in {"http", "https"}
            or not parsed_url.netloc
            or is_loopback
        ):
            frontend_url = settings.DEFAULT_FRONTEND_URL

    return redirect(frontend_url)


urlpatterns = [
    path("", api_home, name="api-home"),
    path("admin/", admin.site.urls),
    path("api/", include("portfolio.urls")),
]
