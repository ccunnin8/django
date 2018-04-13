from django.shortcuts import render
from django.contrib import messages
from ..users.models import User
# Create your views here.
def index(req):
    try:
        users = User.objects.all()
        return render(req,"dashboard/index.html",{"users":users})
    except Exception as e:
        print(e)
        messages.error(req,"Something went wrong")
        return render(req,"dashboard/index.html")
