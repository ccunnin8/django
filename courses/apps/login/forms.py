from django.forms import ModelForm, CharField, PasswordInput
from . import models
class UserForm(ModelForm):
    password_confirm = CharField(widget=PasswordInput)
    class Meta:
        model = models.User
        fields = ("first_name","last_name","email","password")
        widgets = {
            "password": PasswordInput()
        }
