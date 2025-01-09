"""
This module defines the models for the 'companies' application.

Classes:
    CompanyDetail(models.Model): Represents the details of a company.

Dependencies:
    django.db.models: Provides the base classes for defining models.
    django.contrib.auth.models.User: Represents a user in the authentication system.
"""

from django.db import models
from django.contrib.auth.models import User

class CompanyDetail(models.Model):
    """
    Represents the details of a company.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        name (CharField): The name of the company.
        address (TextField): The address of the company.
        contact (CharField): The contact number of the company.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        """
        Returns the string representation of the company, which is its name.

        Returns:
            str: The name of the company.
        """
        return self.name
