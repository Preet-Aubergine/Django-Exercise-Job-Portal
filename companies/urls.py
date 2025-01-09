"""
This module defines the URL patterns for the 'companies' application.

Functions:
    urlpatterns: A list of URL patterns to route URLs to the appropriate views.

Routes:
    details/ -> views.details: Displays the details of a company.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.details, name='details'),
]