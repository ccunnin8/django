from django.shortcuts import render, redirect, reverse
from ..users.models import User
from models import Appointment, Add
from datetime import date
# Create your views here.
def index(req):
    user = User.objects.get(id=req.session["user_id"])
    today = date.today()
    todays_tasks = user.appointments.filter(date=today)
    other_tasks = user.appointments.exclude(date=today)
    return render(req,"appointments/index.html",
    { "user": user, "today": today, "add_apt": Add() , "todays_tasks": todays_tasks, "other_tasks": other_tasks})

def add(req):
    user = User.objects.get(id=req.session["user_id"])
    time = Appointment.objects.create_time(req.POST)
    date = Appointment.objects.create_date(req.POST)
    try:
        Appointment.objects.save(date,time,user,req.POST)
    except Exception as e:
        print(e)
    return redirect(reverse("appointments:index"))
