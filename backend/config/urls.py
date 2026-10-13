from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=settings.FRONTEND_URL, permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
]
