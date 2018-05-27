from __future__ import unicode_literals

from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.forms import CharField, ModelForm, PasswordInput, DateInput, DateField, TextInput
import bcrypt


#manager
class UserManager(models.Manager):
    def encrypt_password(self,password):
        return bcrypt.hashpw(password.encode(),bcrypt.gensalt())

    def check_password(self,password,password2):
        return bcrypt.checkpw(password.encode(),password2.encode())

    def valid_date_format(self,date):
        date_format = "%Y-%m-%d"
        try:
            return datetime.strptime(date,date_format)
        except Exception as e:
            raise ValidationError("Date must be in proper format")


    def login(self,session,user):
        session["logged_in"] = True
        session["user"] = user.email
        session["user_id"] = user.id

    def logout(self,session):
        del session["logged_in"]
        del session["user"]
        del session["user_id"]

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255,validators=[MinLengthValidator(8)])
    birthdate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ["name","email","password"]

    def is_valid(self,date):
        try:
            birthdate = User.objects.valid_date_format(date)
        except Exception as e:
            return False
        return super(UserForm,self).is_valid()
