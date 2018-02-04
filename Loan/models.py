from django.db import models
from django.contrib.auth.models import AbstractUser

class Advisor(AbstractUser):
    referred_by = models.BigIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', null=True, blank=True, default='avatar.jpg')

    def __str__(self):
        return self.designation
