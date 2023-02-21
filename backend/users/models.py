from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    tier = models.ForeignKey('tiers.Tier', on_delete=models.SET_NULL, related_name='tiers', null=True)
