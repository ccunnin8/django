from __future__ import unicode_literals
from ..users.models import User
from django.db import models
from django.forms import ModelForm, DateField, SelectDateWidget, TimeField, Select, CharField
from datetime import time,date
# Create your models here.
class AppManager(models.Manager):
    def create_time(self,post):
    #takes post, returns time
        hour = int(post['hour'])
        minute = int(post['minute'])
        am_or_pm = post['am_or_pm']
        if post['am_or_pm'] == "PM":
            if hour != 12:
                hour += 12
        elif post["am_or_pm"] == "AM":
            if hour == 12:
                hour = 0
        return time(hour,minute)

    def create_date(self,post):
    #takes post, returns date
        month = int(post['date_month'])
        day = int(post['date_day'])
        year = int(post['date_year'])
        return date(year,month,day)

    def save(self,date,time,user,post):
    #takes date, time that are already processed, with the current user, and the rest of post and makes appt
        super(AppManager,self).create(user=user,date=date,time=time,tasks=post['tasks'])


class Appointment(models.Model):
    PENDING = "P"
    COMPLETE = "C"
    MISSED = "M"
    APPT_STATUS_CHOICES = (
        ("Pending",PENDING),
        ("Complete",COMPLETE),
        ("Missed",MISSED)
    )

    tasks = models.CharField(max_length=255)
    status = models.CharField(max_length=15,choices=APPT_STATUS_CHOICES,default=PENDING)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User,related_name="appointments")
    objects = AppManager()





class Add(ModelForm):
    hours = tuple([(num,'0' + str(num)) if num < 10 else (num,str(num)) for num in range(1,13)])
    minutes = tuple([(num,'0' + str(num)) if num < 10 else (num,str(num)) for num in range(0,60)])
    am_pm = (('AM','AM'),('PM','PM'))
    date = DateField(input_formats=["%Y-%m-%d"], widget=SelectDateWidget)
    hour = DateField(widget=Select(choices=hours))
    minute = DateField(widget=Select(choices=minutes))
    am_or_pm = CharField(widget=Select(choices=am_pm))
    class Meta:
        model = Appointment
        fields = ["date","time","tasks"]
