
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def api_home(request):
    return JsonResponse({
        "message": "Django Portfolio API is running",
        "status": "ok",
        "projects_endpoint": "/api/",
    })


urlpatterns = [
    path("", api_home, name="api-home"),
    path("admin/", admin.site.urls),
    path("api/", include("portfolio.urls")),
]
