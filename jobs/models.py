"""
This module defines the models for the 'jobs' application.

Classes:
    JobPost(models.Model): Represents a job posting.

Dependencies:
    django.db.models: Provides the base classes for defining models.
    django.contrib.auth.models.User: Represents a user in the authentication system.
"""
from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
    """
    Represents a job posting.

    Attributes:
        user (ForeignKey): A foreign key relationship to the User model.
        name (CharField): The name of the job.
        desc (TextField): The description of the job.
        location (CharField): The location of the job.
        salary_from (DecimalField): The minimum salary for the job.
        salary_to (DecimalField): The maximum salary for the job.
        tags (CharField): Tags associated with the job.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    desc = models.TextField()
    location = models.CharField(max_length=255)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2) 
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255)  

    def __str__(self):
        """
        Returns the string representation of the job post, which is its name.

        Returns:
            str: The name of the job.
        """
        return self.name

