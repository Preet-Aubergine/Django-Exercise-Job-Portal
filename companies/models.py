from django.db import models
from django.contrib.auth.models import User

class CompanyDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
