from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    desc = models.TextField()
    location = models.CharField(max_length=255)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2) 
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255)  

    def __str__(self):
        return self.name

