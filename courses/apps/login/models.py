from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from re import search


def password_validation(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 Characters")
    if not search(r'[A-Z]{1,}',password):
        raise ValidationError("Must contain at least 2 capital letters")
    if not search(r'[a-z]{1,}',password):
        raise ValidationError("Must contain at least 2 lowercase letters")
    if not search(r'[!@#$%^&*()]{1}',password):
        raise ValidationError("Must contain at least 1 special character")
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, validators=[password_validation])
