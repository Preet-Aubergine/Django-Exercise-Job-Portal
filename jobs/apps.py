"""
This module defines the configuration for the 'jobs' application.

Classes:
    JobsConfig(AppConfig): Configuration class for the 'jobs' application.

Attributes:
    default_auto_field (str): Specifies the type of primary key to use for models in this app.
    name (str): The name of the application.
"""

from django.apps import AppConfig

class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'
