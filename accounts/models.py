from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'


#password:superadmin(admin,admin@example.com)
# user:kage(kage@kage.com,summerdevelop)    
