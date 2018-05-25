from django.shortcuts import render
from ..users.models import User
from models import Appointment, Add
from datetime import date
# Create your views here.
def index(req):
    user = User.objects.get(id=req.session["user_id"])
    today = date.today()
    return render(req,"appointments/index.html", { "user": user, "today": today, "add_apt": Add() })
