from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from bcrypt import hashpw, gensalt
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

def encrypt_password(password):
    return hashpw(password.encode(),gensalt())

class UserManager(models.Manager):
    errors = []
    def validate(self,post_data):
        if "first_name" in post_data:
            self.first_name(post_data.first_name)
        if "last_name" in post_data:
            self.last_name(post_data.last_name)
        if "email" in post_data:
            self.email(post_data.email)
        if "password" in post_data:
            self.password(post_data.password)
        return errors

    def first_name(self,name):
        if len(name) < 2:
            self.errors.append("First name must be longer than 2 characters")

    def last_name(self,name):
        if len(name) < 2:
            errors.append("First name must be longer than 2 characters")

    def email(self,name):
        email_validator = EmailValidator()
        try:
            email_validator(email)
        except ValidationError, e:
            self.errors.append(e)

    def password(self,password):
        try:
            password_validation(password)
        except ValidationError, e:
            self.errors.append(e)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255,validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=255,validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255,validators=[password_validation])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
    objects = UserManager()

    def save(self,*args,**kwargs):
        self.password = encrypt_password(self.password)
        super(User,self).save(*args,**kwargs)


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
