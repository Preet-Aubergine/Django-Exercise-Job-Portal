"""
This module registers the models for the 'companies' application with the Django admin site.

Dependencies:
    django.contrib.admin: Provides the admin interface.
    .models.CompanyDetail: The model representing company details.

Registrations:
    admin.site.register(CompanyDetail): Registers the CompanyDetail model with the admin site.
"""

from django.contrib import admin
from .models import CompanyDetail

# Register your models here.
admin.site.register(CompanyDetail)
