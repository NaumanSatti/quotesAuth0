from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Quote(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote=models.TextField(null=True, blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
