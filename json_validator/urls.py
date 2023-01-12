"""
URLs for the json_validator app.
"""
from django.urls import path
from django.views.generic.base import TemplateView

from .views import ValidateData

urlpatterns = [
    path(r'', TemplateView.as_view(template_name='main.html'), name='home'),
    path('validate/', ValidateData.as_view(), name='validate_data')
]
