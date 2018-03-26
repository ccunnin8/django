from __future__ import unicode_literals

from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import bcrypt
class UserManager(models.Manager):

    def validate(self,post_data):
        if "email" in post_data:
            self.validate_email(post_data["email"])
        else:
            raise ValidationError("Must include an email")
        if "name" in post_data:
            self.validate_name(post_data["name"])
        else:
            raise ValidationError("Must include a name")
        if "alias" in post_data:
            self.validate_name(post_data["alias"])
        else:
            raise ValidationError("Must include an alias!")
        if "password" in post_data:
            self.validate_password(post_data["password"])
        else:
            raise ValidationError("Must include a password!")

    def validate_email(self,email):
        email_val = EmailValidator()
        email_val(email)

    def validate_name(self,name):
        if len(name) < 2:
            raise ValidationError("Name and alias Must be longer than 2 characters")

    def validate_password(self,password):
        if len(password) < 8:
            raise ValidationError("Password must be 8 or more characters")

    def encrypt_password(self,password):
        return bcrypt.hashpw(password.encode(),bcrypt.gensalt())

    def check_password(self,password,password2):
        return bcrypt.checkpw(password.encode(),password2.encode())

    def create_user(self,post_data):
        return self.create(
            name = post_data["name"],
            alias = post_data["alias"],
            email = post_data["email"],
            password = self.encrypt_password(post_data["password"]))
        

    def login(self,session,user):
        session["logged_in"] = True
        session["user"] = user.email
        session["user_id"] = user.id

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
