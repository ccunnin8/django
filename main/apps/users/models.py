from django.db.models import Model, CharField, IntegerField, DateTimeField

# Create your models here.
class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email_address = CharField(max_length=255)
    age = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return "{x} {y} is {age}, email = {email}".format(x=self.first_name,y=self.last_name,age=self.age,email=self.email_address)

    def print_names(self):
        for user in self.objects.order_by("first_name"):
            print(user.first_name)
