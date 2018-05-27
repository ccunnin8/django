from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
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

def edit(req,id):
    try:
        appt = Appointment.objects.get(id=id)
        if appt.user.id != req.session["user_id"]:
            raise Exception("appointment does not belong to user")
        response = {
            "hour": str(appt.time.hour) if appt.time.hour < 12 else str(appt.time.hour - 12),
            "minute": str(appt.time.minute),
            "month": str(appt.date.month),
            "year": str(appt.date.year),
            "day": str(appt.date.day),
            "tasks": appt.tasks,
            "am_or_pm": "AM" if appt.time.hour < 12 else "PM",
            "id": appt.id
        }
        return JsonResponse(response)
    except Exception as e:
        return redirect(reverse("appointments:index"))

def delete(req,id):
    try:
        appointment = Appointment.objects.get(id=id)
    except:
        return redirect(reverse("appointments:index"))
    if appointment.user.id  == req.session["user_id"]:
        appointment.delete()
    return redirect(reverse("appointments:index"))

def update(req):
    try:
        app = Appointment.objects.get(id=req.POST["appointment_id"])
        if app.user.id != req.session["user_id"]:
            raise Exception("User not authorized")
        app.time = Appointment.objects.create_time(req.POST)
        app.date = Appointment.objects.create_date(req.POST)
        app.tasks = req.POST["tasks"]
        app.save()
    except Exception as e:
        print(e)
    return redirect(reverse("appointments:index"))
