from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate, get_user
from django.contrib.auth.decorators import login_required
from ..users.forms import UserForm

# Create your views here.
def index(req):
    return render(req,"main/index.html")

def signin(req):
    return render(req,"main/signin.html")

def register(req):
    form = UserForm().as_p
    return render(req,"main/register.html", {"user_form": form })

def login(req):
    #get post info password, email
    user = authenticate(username=req.POST["username"],password=req.POST["password"])
    if user is not None:
        auth_login(req,user)
        return redirect(reverse("dashboard:index"))
    else:
        #user is not found
        messages.error(req,"User not found or Password Incorrect!")
        return redirect(reverse("index:signin"))

@login_required(login_url="index:signin")
def logout(req):
    #if a user is logged in or exists delete the session key
    user = get_user(req)
    auth_logout(req)
    return redirect(reverse("index:signin"))
