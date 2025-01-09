"""
This module defines the URL patterns for the 'accounts' application.

Functions:
    urlpatterns: A list of URL patterns to route URLs to the appropriate views.

Routes:
    register/ -> views.register: Handles user registration.
    login/ -> views.login: Handles user login.
    logout/ -> views.logout: Handles user logout.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]