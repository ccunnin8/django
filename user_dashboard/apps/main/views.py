from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from user_dashboard.applications.users.models import User
from datetime import date
from bcrypt import checkpw
# Create your views here.
def index(req):
    if "form_errors" in req.session:
        req.session["form_errors"] = []
    return render(req,"main/index.html")

def signin(req):
    return render(req,"main/signin.html")

def register(req):
    return render(req,"main/register.html")

def login(req):
    try:
        #get post info password, email
        email = req.POST["email"]
        password = req.POST["password"]
        #try to get user (catch error if user not found), get user's password
        user = User.objects.get(email=email)
        user_password = user.password
        #use bcrypt to see if password matches hashed password
        if checkpw(password.encode(),user_password.encode()):
            #add user to session
            req.session["user"] = {
                "id": user.id,
                "email": user.email,
                "created_at": user.created_at.date().strftime("%Y %M %D"),
                "admin": user.admin
            }
            #user is logged in
            req.session["logged_in"] = True
        else:
            #password is not correct
            messages.error(req,"Incorrect Password")
            return redirect(reverse("index:signin"))
        #user is an admin
        if user.admin:
            return redirect(reverse("dashboard:admin_dashboard"))
        #user is not an admin
        else:
            return redirect(reverse("dashboard:index"))
    except:
        #user is not found
        messages.error(req,"User not found!")
        return redirect(reverse("index:signin"))

def logout(req):
    #if a user is logged in or exists delete the session key
    if "user" in req.session:
        del req.session["user"]
        del req.session["logged_in"]
        return redirect(reverse("index:signin"))
    else:
        messages.error(req,"No user logged in")
        return redirect(reverse("index:signin"))
