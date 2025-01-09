"""
This module defines the URL patterns for the 'portal' application.

Functions:
    urlpatterns: A list of URL patterns to route URLs to the appropriate views.

Routes:
    / -> views.index: Displays the index page of the portal.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index')
]