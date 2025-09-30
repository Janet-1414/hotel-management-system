from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Staff(AbstractUser):
    ROLES = [
        ('MANAGER', 'Manager'),
        ('RECEPTIONIST','Receptionist')
    ]
    role = models.CharField(max_length=20, choices= ROLES, default='RECEPTIONIST')
    def __str__(self):
        return self.username
    

