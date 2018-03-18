from django.db.models import Model, CharField, IntegerField, DateTimeField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, EmailValidator
import re
# Create your models here.
class User(Model):
    first_name = CharField(max_length=255,validators=[MinLengthValidator(2)])
    last_name = CharField(max_length=255,validators=[MinLengthValidator(2)])
    email_address = CharField(max_length=255,unique=True,validators=[EmailValidator])
    age = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return "{x} {y} is {age}, email = {email}".format(x=self.first_name,y=self.last_name,age=self.age,email=self.email_address)

    #this is not really the way data should be validated, but it
    #is the only way to get django to validate the data before saving it!
    def clean(self):
        if len(self.first_name) < 2:
            raise ValidationError("Name must be greater than 2")
        if len(self.last_name) < 2:
            raise ValidationError("Name must be greater than 2")
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.email_address):
            raise ValidationError("Email not valid")
    def save(self, *args, **kwargs):
        self.clean()
        super(User,self).save(*args,**kwargs)

    def print_names(self):
        for user in self.objects.order_by("first_name"):
            print(user.first_name)
