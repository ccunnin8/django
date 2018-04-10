from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import User, Comment, Message
from django.contrib.auth import authenticate, login, get_user, user_login_failed
from django.contrib.auth.decorators import login_required
from forms import UserForm
# Create your views here.

def index(req):
    user = get_user(req)
    if user.is_authenticted():
        if user.is_staff:
            return redirect(reverse("dashboard:admin_dashboard"))
        else:
            return redirect(reverse("dashboard:index"))
    else:
        return redirect(reverse("index:index"))

@login_required(login_url="index:signin")
def new(req):
    user = get_user(req)
    if user.is_staff:
        return render(req,"users/register.html")
    else:
        messages.error(req,"You are not authorized to view this page")
        return render(reverse("dashboard:index"))

def create(req):
    #make user object from model form
    user = UserForm(req.POST)
    if user.is_valid():
        user = user.save(commit=False)
        #if it's the first user make it an admin
        user.is_staff = len(User.objects.all()) == 0
        user.save()
        #redirect to the users page
        login(req,user)
        return redirect(reverse("users:show",kwargs={"id": user.id}))
    else:
        messages.error(req,user.errors)
        #show errors and redirect
        return redirect(reverse("index:register"))

@login_required(login_url="index:signin")
def delete_conf(req,id):
    try:
        user = User.objects.get(id=id)
        context = {
            "id": user.id
        }
    except Exception as e:
        print(e)
        messages.error(req,"Something went wrong!")
        if req.session["admin"]:
            return redirect(reverse("dashboard:admin_dashboard"))
        else:
            return redirect(reverse("dashboard:index"))
    return render(req,"users/confirm_delete.html",context)

@login_required(login_url="index:signin")
def destroy(req,id):
    #if the user being deleted is the user logged in OR the user is an admin delete, try to delete the user
    user = get_user(req)
    if user.id == id or user.is_staff:
        try:
            User.objects.get(id=id).delete()
            return redirect(reverse("main:index"))
        except Exception as e:
            print(e)
            messages.error(req,"something went wrong")
            if req.session["admin"]:
                return redirect(reverse("dashboard:admin_dashboard"))
            else:
                return redirect(reverse("dashboard:index"))

def update(req,id):
    req = "this will update user " + str(id)
    return HttpResponse(id)

def show(req,id):
    try:
        user = User.objects.get(id=id)
        return render(req,"users/show.html",{"user":user})
    except Exception as e:
        print(e)
        messages.error(req,"User not found")
        if req.session["logged_in"]:
            if req.session["admin"]:
                return redirect(reverse("dashboard:admin_dashboard"))
            else:
                return redirect(reverse("dashboard:index"))
        else:
            return redirect(reverse("index:index"))

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
