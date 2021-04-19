from django.contrib.auth.models import User
from django.db import models
from model_controller.models import AbstractModelController

from .choices import Role


class Profile(AbstractModelController):
    role = models.IntegerField(choices=Role.choices, default=Role.GENERAL)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
