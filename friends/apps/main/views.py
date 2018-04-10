from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from ..users.models import User, UserForm

# Create your views here.
def index(req):
    return render(req,"main/index.html")

def create(req):
    #check to see if passwords match on form
    if req.POST["password"] != req.POST["password_conf"]:
        messages.error(req,"Passwords do not match!")
        return redirect(reverse("main:index"))
    #if they do use the UserForm to validate data and try to insert a new user
    else:
        try:
            User.objects.validate(req.POST)
            user = User.objects.create(req.POST)
            User.objects.login(req.session,user)
            return redirect(reverse("friends:index"))
        except Exception as e:
            for error in e:
                messages.error(req,error)
            return redirect(reverse("main:index"))
        else:
            return render(req,"main/index.html")

def login(req):
    try:
        user = User.objects.get(email=req.POST["email"])
        if User.objects.check_password(req.POST["password"],user.password):
            User.objects.login(req.session,user)
            return redirect(reverse("friends:index"))
        else:
            messages.error(req,"Incorrect Password!")
            return redirect(reverse("main:index"))
    except Exception as e:
        print(e)
        messages.error(req,"User not found!")
        return redirect(reverse("main:index"))

def logout(req):
    if "logged_in" in req.session:
        if req.session["logged_in"]:
            User.objects.logout(req.session)
        else:
            message.error(req,"Not logged in")
    else:
        messages.error(req,"Not logged in")
    return redirect(reverse("main:index"))
