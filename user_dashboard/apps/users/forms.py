from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]


class ChangeInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
