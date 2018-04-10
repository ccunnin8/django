from __future__ import unicode_literals
from django.core.validators import EmailValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def password_validation(blah):
    pass

# Create your models here.
class UserProfile(models.Model):
    description = models.TextField()
    user = models.OneToOneField(User,related_name="user_profile")

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User,related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
