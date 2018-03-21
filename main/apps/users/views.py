from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from apps.users.forms import UserForm
from apps.users.models import User

def edit(req,id):
    edit_user = UserForm()
    return render(req,"users/edit.html",{"id": id, "edit_user": edit_user})

def show(req,id):
    try:
        user = User.objects.get(id=id)
        return render(req,"users/show.html",{"user":user})
    except:
        messages.error(req,"User not found")
        return redirect(reverse("users:index"))

def create(req):
    try:
        new_user = UserForm(req.POST)
        print(new_user)
        new_user.save()
        return redirect(reverse("users:index"))
    except:
        messages.error(req,"Unable to create new user")
        return redirect(reverse("users:index"))

def destroy(req,id):
    try:
        User.objects.get(id=id).delete()
        return redirect(reverse("users:index"))
    except:
        messages.error(req,"Unable to delete user")
        return redirect(reverse("users:index"))

def update(req):
    try:
        id = req.POST["id"]
        old_instance = User.objects.get(id=id)
        updated = UserForm(req.POST,instance=old_instance)
        updated.save()
        return redirect(reverse("users:index"))
    except:
        messages.error(req,"There was an error updating user")
        return redirect(reverse("users:index"))

def index(req):
    all_users = User.objects.all()
    for user in all_users:
        user.set_full_name()
    return render(req,'users/index.html',{"users":all_users})

def new(req):
    create_user = UserForm()
    return render(req,'users/new.html',{"new_user": create_user})
