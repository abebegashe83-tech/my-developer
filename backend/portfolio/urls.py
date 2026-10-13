from django.urls import path

from .views import contact_message, health_check, project_list

urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('projects/', project_list, name='project-list'),
    path('contact/', contact_message, name='contact-message'),
]
