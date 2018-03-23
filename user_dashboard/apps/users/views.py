from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import User, Comment, Message
from forms import UserForm
from datetime import date
from bcrypt import checkpw
# Create your views here.
def index(req):
    if "logged_in" in req.session:
        if req.session["logged_in"]:
            if req.session["user"].admin:
                return redirect(reverse("dashboard:admin_dashboard"))
            else:
                return redirect(reverse("dashboard:index"))
        else:
            return redirect(reverse("index:index"))

def new(req):
    return render(req,"users/register.html")

def create(req):
    #check to see if password and password_conf are the same
    if req.POST["password"] != req.POST["password_conf"]:
        messages.error(req,"Your passwords do not match!")
        return redirect(reverse("index:register"))
    try:
        #make user object from model form
        new_user = UserForm(req.POST)
        user = new_user.save()
        #if it's the first user make it an admin
        if len(User.objects.all()) == 1:
            user.admin = True
            user.save()
        #clear out form errors because it was a success!
        req.session["form_errors"] = []
        #redirect to the users page
        return redirect(reverse("users:show",kwargs={"id": user.id}))
    except:
        #show errors and redirect
        messages.error(req,"There was an error registering please try again")
        req.session["form_errors"] = new_user.errors
        return redirect(reverse("index:register"))


def destroy(req,id):
    req = "this is a test " + str(id)
    return HttpResponse(id)

def update(req,id):
    req = "this will update user " + str(id)
    return HttpResponse(id)

def show(req,id):
    return render(req,"users/show.html")

def edit(req):
    return render(req,"users/edit.html")

def edit_admin(req,id):
    return render(req,"users/edit_admin.html")

def message(req,id):
    req = "will post a comment to " + str(id)
    return HttpResponse(req)

def comment(req,user_id,comment_id):
    req = "will post a comment to user: " + str(user_id) + "on comment " + str(comment_id)
    return HttpResponse(req)
