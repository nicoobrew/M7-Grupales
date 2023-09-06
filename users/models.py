from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    # nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    # email = models.EmailField()
    # grupo = models.CharField(max_length=50)

    def __str__(self):
        # return self.nombre
        return self.username

# class CustomUser2(AbstractUser):
#     username = None
#     rut = models.CharField(max_lenth=12, unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         self.rut