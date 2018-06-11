from __future__ import unicode_literals
from django.db import models
from ..users.models import User
from django.core.exceptions import ValidationError
import re

def phone_validation(self,phonenumber):
    if not re.match(r'[0-9]{3}-[0-9]{3}-[0-9]{4}',self.phonenumber):
        raise ValidationError("phone number must be in 000-000-0000 format!")

# Create your models here.
class Settings(models.Model):
    email = models.BooleanField(default=False)
    txt = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=12,validators=[phone_validation])
    user = models.OneToOneField(User,related_name="settings")
