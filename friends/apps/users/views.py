from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from ..users.models import User
# Create your views here.
def index(req):
    return redirect(reverse("friends:index"))

def show(req,id):
    try:
        user = User.objects.get(id=id)
        return render(req,"users/index.html",{"user":user})
    except Exception as e:
        print(e)
        messages.error(req, "User not found!")
        return redirect(reverse("friends:index"))
