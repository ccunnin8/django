from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..users.models import User
# Create your views here.
def index(req):
    return render(req,"main/index.html")

def register(req):
    req.session["errors"] = {}
    if req.POST["password"] != req.POST["password_conf"]:
        messages.error(req,"passwords do not match!")
        return redirect("/")
    else:
        try:
            User.objects.validate(req.POST)
        except Exception as e:
            print(e)
            messages.error(req,e[0])
            return redirect("/")
        try:
            user = User.objects.create_user(req.POST)
            User.objects.login(req.session,user)
            print("logged_in")
            return redirect("/books")
        except Exception as e:
            print(e)
            messages.error(req,"Something went wrong!")
            return redirect("/")


def login(req):
    email = req.POST["email"]
    password = req.POST["password"]
    try:
        user = User.objects.get(email=email)
    except Exception as e:
        messages.error(req,e[0])
        return redirect("/")
    if User.objects.check_password(password,user.password):
        User.objects.login(req.session,user)
        return redirect("/books")
    else:
        messages.error(req,"Invalid Password")
        return redirect("/")

def logout(req):
    try:
        del req.session["logged_in"]
        del req.session["user"]
        del req.session["user_id"]
        return redirect("/")
    except:
        messages.error(req,"Something went wrong!")
        return redirect("/")

def logged_in(inner_function):
    def function(req):
        if req.session["logged_in"]:
            return inner_function(req)
        else:
            messages.error(req,"You must be logged in!")
            return redirect("/")
