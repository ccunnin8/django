from django.test import TestCase
from django.test import Client
from django.shortcuts import reverse
from django.db import transaction
from .models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib import messages
import bcrypt
# Create your tests here.

client = Client()

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            name="test",
            email="test@test.com",
            password= bcrypt.hashpw("12345678".encode(),bcrypt.gensalt()),
            birthdate = datetime.strptime("1988-03-14","%Y-%m-%d")
        )

    def test_name(self):
        user = User.objects.get(name="test")
        self.assertEqual(user.name,"test")

    def test_user(self):
        try:
            with transaction.atomic():
                client.post(reverse("main:register"),{
                    'name': "john",
                    'email': "coreyjjc@test.com",
                    'password': "12345678",
                    'password_confirmation': "12345678",
                    'birthdate':  "1988-03-14"
                })
                self.assertEqual(User.objects.get(email="coreyjjc@test.com").name,"john")
        except:
            print("FAIL")

    def test_submission_with_duplicate_email(self):
        try:
            res = client.post(reverse("main:register"), {
                'name': "john",
                'email': "test@test.com",
                'password': "12345678",
                'password_confirmation': "12345678",
                'birthdate':  "1988-03-14"
            })
        except:
            self.assertRaises(ValidationError)
        self.assertEqual(1,len(User.objects.all()))

    def test_submission_with_incorrect_date(self):
        try:
            res = client.post(reverse("main:register"), {
                'name': "john",
                'email': "test@tester.com",
                'password': "12345678",
                'password_confirmation': "12345678",
                'birthdate':  "03/14/1988"
            })
        except:
            self.assertRaises(ValidationError)

    def test_login(self):
        res = client.post(reverse("main:login"),{
            "email": "test@test.com",
            "password": "12345678"
        })
        self.assertRedirects(res,reverse("appointments:index"))
        
        self.assertEqual(client.session["logged_in"],True)

    def test_login_fail(self):
        res = client.post(reverse("main:login"),{
            "email": "doesntexist@gmail.com",
            "password": "doesntexist"
        })
        self.assertRedirects(res,reverse("main:index"))
