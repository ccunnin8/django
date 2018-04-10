from __future__ import unicode_literals

from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.forms import ModelForm
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def encrypt_password(self,password):
        return bcrypt.hashpw(password.encode(),bcrypt.gensalt())

    def login(self,session,user):
        session["user_email"] = user.email
        session["user_name"] = user.name
        session["user_id"] = user.id
        session["logged_in"] = True

    def logout(self,session):
        del session["user_email"]
        del session["user_name"]
        del session["user_id"]
        del session["logged_in"]

    def check_password(self,password,password1):
        return bcrypt.checkpw(password.encode(),password1.encode())

    def valid_date_format(self,date):
        date_format = "%m/%d/%Y"
        try:
             return datetime.strptime(date,date_format)
        except Exception as e:
            print(e)
            raise ValidationError("Date must be in proper format")

    def validate_password(self,password):
        if len(password) < 8:
            raise ValidationError("Password Must Be Longer than 8 Characters!")

    def validate_name(self,name):
        if len(name) < 3:
            raise ValidationError("Name Must Be Longer Than 3 Characters!")

    def validate(self,post_data):
        if "name" in post_data:
            self.validate_name(post_data["name"])
        else:
            raise ValidationError("Must Include Name!")
        if "alias" in post_data:
            try:
                self.validate_name(post_data["alias"])
            except:
                raise ValidationError("Alias must be longer than 3 characters!")
        else:
            raise ValidationError("Must Include Alias!")
        if "email" in post_data:
            EmailValidator(post_data["email"])
        else:
            raise ValidationError("Email must be included!")
        if "password" in post_data:
            self.validate_password(post_data["password"])
        else:
            raise ValidationError("Password Required!")
        if "birthday" in post_data:
            self.valid_date_format(post_data["birthday"])
        else:
            raise ValidationError("Must include birthday in (MM/DD/YYYY format)!")
        return self

    def create(self,post_data):
        return super(UserManager,self).create(
            name = post_data["name"],
            alias = post_data["alias"],
            email = post_data["email"],
            password = self.encrypt_password(post_data["password"]),
            birthdate = self.valid_date_format(post_data["birthday"])
        )


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthdate = models.DateField()
    objects = UserManager()

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name","alias","password",'birthdate']

    def save(self,commit=True):
        user = super(UserForm,self).save(commit=False)
        user.password = User.objects.encrypt_password(user.password)
        if commit:
            user.save()
        return user
