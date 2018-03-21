from django.shortcuts import render, HttpResponse,redirect
from . import forms
from . import models
from django.contrib import messages
from bcrypt import hashpw, gensalt, checkpw

# Create your views here.
def index(req):
    UserForm = forms.UserForm()
    return render(req,'login/index.html',{"UserForm":UserForm})

def create(req):
    if req.POST["password"] != req.POST["password_confirm"]:
        messages.error(req,"Your passwords do not match!")
        return redirect("/")
    else:
        try:
            user = forms.UserForm(req.POST).save(commit=False)
            user.password = hashpw(user.password.encode(),gensalt())
            user.save()
            return redirect("/success")
        except:
            messages.error(req,"We encountered an error please see form for details")
            print forms.UserForm(req.POST).errors
            return render(req,"login/index.html",{
                "UserForm": forms.UserForm(),
                "errors": forms.UserForm(req.POST).errors
            })

def login(req):
    email = req.POST["email"]
    password = req.POST["password"]
    try:
        user = models.User.objects.get(email=email)
        if checkpw(password.encode(),user.password.encode()):
            req.session["user"] = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
            return redirect('/success')
        else:
            messages.error(req,"Password incorrect!")
            return redirect('/')
    except:
        messages.error(req,"Username not found!")
        return redirect('/')

def success(req):
    return render(req,'login/success.html')
