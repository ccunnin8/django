from django.forms import ModelForm
from . import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['first_name','last_name','email_address','age']
