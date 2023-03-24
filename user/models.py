from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    area = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
        
   
    class Meta:
        db_table = 'user'   
    