from django.test import TestCase
from .models import Appointment
from ..user.models import User
from datetime import date, time
# Create your tests here.

class AppointmentTests(TestCase):
    def setUp(self):
        user = User.objects.create(
            name="corey",
            email="corey@gmail.com",
            birthdate=date(03,14,1988),
            password=User.objects.encrypt_password("12345678")
        )
        app = Appointment.objects.create(
            user=user,
            date=date(06,18,2018),
            time=time(11,00),
            tasks="board plane"
        )

    def test_
