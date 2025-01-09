"""
This module defines the configuration for the 'users' application.

Classes:
    UsersConfig(AppConfig): Configuration class for the 'users' application.

Attributes:
    default_auto_field (str): Specifies the type of primary key to use for models in this app.
    name (str): The name of the application.
"""
from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Configuration class for the 'users' application.

    Attributes:
        default_auto_field (str): Specifies the type of primary key to use for models in this app.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
