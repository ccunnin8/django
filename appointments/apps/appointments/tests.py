from django.test import TestCase, Client
from django.shortcuts import reverse
from models import Appointment
from ..users.models import User
from datetime import date, time
# Create your tests here.

class AppointmentTests(TestCase):
    def setUp(self):
        client = Client()
        self.post = {
            "hour": "12",
            "minute": "00",
            "date_month": "03",
            "date_day": "14",
            "date_year": "1988",
            "tasks": "This is a test!",
            "am_or_pm": "PM"
        }
        self.test_user = User.objects.create(name="test", email="test@test.com", birthdate=date(1988,03,14),password=User.objects.encrypt_password("12345678"))
    #HELPER FUNCTION TO SIMULATE LOGGEDIN USER
    def login(self):
        #simulate logged in user
        session = self.client.session
        session["user_id"] = self.test_user.id
        session.save()

    def test_create_time(self):
        test_time = time(12,00)
        self.assertEqual(Appointment.objects.create_time(self.post),test_time)
        post = {
            "hour": "01",
            "minute": "23",
            "am_or_pm": "AM"
        }
        test_time = time(01,23)
        self.assertEqual(Appointment.objects.create_time(post),test_time)
        post = {
            "hour": "12",
            "minute": "23",
            "am_or_pm": "AM"
        }
        test_time = time(00,23)
        self.assertEqual(Appointment.objects.create_time(post),test_time)
        post = {
            "hour": "9",
            "minute": "23",
            "am_or_pm": "PM"
        }
        test_time = time((9+12),23)
        self.assertEqual(Appointment.objects.create_time(post),test_time)
        post = {
            "hour": "12",
            "minute": "59",
            "am_or_pm": "PM"
        }
        test_time = time(12,59)
        self.assertEqual(Appointment.objects.create_time(post),test_time)

    def test_create_date(self):
        test_date = date(1988,03,14)
        self.assertEqual(Appointment.objects.create_date(self.post),test_date)

    def test_save(self):
        t = Appointment.objects.create_time(self.post)
        d = Appointment.objects.create_date(self.post)
        Appointment.objects.save(d,t,self.test_user,self.post)
        new_appt = Appointment.objects.all()[0]
        self.assertEqual(self.test_user.id,new_appt.user.id)

    def test_index(self):
        self.login()
        #use previous test to add an appointment to the suer
        self.test_save()
        #get appointments index page
        response = self.client.get(reverse("appointments:index"))
        self.assertEqual(response.status_code,200) #RESPONSE 200 OK
        self.assertEqual(len(response.context["other_tasks"]),1) #1 APPOINTMENT IN OTHER_TASKS
        self.assertEqual(response.context["other_tasks"][0].tasks,"This is a test!") #TASK IN OTHER_TASKS is what we expect


    def test_add(self):
        self.login()
        current_appointments = len(self.test_user.appointments.all())
        new_post = dict(self.post)
        new_post["tasks"] = "This is another task!"
        self.client.post(reverse("appointments:add"), new_post)
        self.assertEqual(current_appointments + 1,len(self.test_user.appointments.all()))

    def test_delete(self):
        self.login()
        self.test_add()
        response = client.delete(reverse("appointments:delete", args=[1]))
        assertEqual(0,len(self.test_user.appointments.all()))
        assertEqual(response.status_code,302)

    def test_edit(self):
        self.login()
        self.test_add()
        
