from __future__ import unicode_literals
from ..users.models import User
from django.db import models
from django.forms import ModelForm, DateField
# Create your models here.
class Appointment(models.Model):
    PENDING = "P"
    COMPLETE = "C"
    MISSED = "M"
    APPT_STATUS_CHOICES = (
        (PENDING, "Pending"),
        (COMPLETE, "Complete"),
        (MISSED,"Missed")
    )

    tasks = models.CharField(max_length=255)
    status = models.CharField(max_length=15,choices=APPT_STATUS_CHOICES,default=PENDING)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User,related_name="appointments")

class Add(ModelForm):
    date = DateField(input_formats=["%m/%d/%y"])
    class Meta:
        model = Appointment
        fields = ["date","time","tasks"]
