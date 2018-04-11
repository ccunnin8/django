from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]


class ChangePassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ["password"]

class ChangeInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
