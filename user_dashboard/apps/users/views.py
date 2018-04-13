from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import User, Comment, Message, UserProfile
from django.contrib.auth import authenticate, login, get_user, user_login_failed
from django.contrib.auth.decorators import login_required
from forms import UserForm, ChangeInfo
from django.contrib.auth.forms import PasswordChangeForm as ChangePassword
# Create your views here.

@login_required(login_url="index:index")
def index(req):
    return redirect(reverse("dashboard:index"))

@login_required(login_url="index:signin")
def new(req):
    user = get_user(req)
    if user.is_staff:
        return render(req,"users/register.html", {"user_form": UserForm().as_p })
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
        #if we create as user as an admin skip logging in
        if not get_user(req).is_authenticated:
            login(req,user)
        #redirect to the users page
        return redirect(reverse("users:show",kwargs={"id": user.id}))
    else:
        messages.error(req,user.errors)
        #show errors and redirect
        return redirect(reverse("index:register"))

@login_required(login_url="index:signin")
def delete_conf(req,id):
    try:
        user = User.objects.get(id=id)
        context = { "id": user.id }
    except Exception as e:
        print(e)
        messages.error(req,"Something went wrong!")
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
            return redirect(reverse("dashboard:index"))

@login_required(login_url="index:signin")
def update(req):
    #get id in session from redirect and delete it
    id = int(req.session["id"])
    del req.session["id"]
    #if the id is the same as the person logged in then user =
    #the user is not me, but i'm an admin so i can edit you
    if get_user(req).id != id and get_user(req).is_staff:
        try:
            user = User.objects.get(id=id)
        except Exception as e:
            messages.error(req,"Unable to retrieve user")
    #the user is me so I can edit me
    elif get_user(req).id == id:
        user = get_user(req)
    #the user i'm editing is not me and I'm not staff -- NOT ALLOWED
    else:
        messages.error(req,"You are not authorized to edit this user!")
        return redirect(reverse("dashboard:index"))
    if user.id == id or get_user(req).is_staff:
        if req.POST["type"] == "password":
            #update passwor
            update_password(req,user)
        elif req.POST["type"] == "info":
            update_info(req,user)
        elif req.POST["type"] == "description":
            update_description(req,user)
        #everything failed!
    return redirect(reverse("dashboard:index"))


def update_password(req,user):
    new_user = ChangePassword(req.POST,instance=user)
    if new_user.is_valid():
        new_user.save()
        return False
    return redirect(reverse("users:edit"))

def update_info(req,user):
    new_user = ChangeInfo(req.POST,instance=user)
    if new_user.is_valid():
        new_user.save()
        return False
    return redirect(reverse("users:edit"))

def update_description(req,user):
    try:
        profile = UserProfile.objects.get(user=user)
        profile.description = req.POST["description"]
        profile.save()
    except:
        UserProfile.objects.create(
            user=user,
            description=req.POST["description"]
        )


@login_required(login_url="index:signin")
def show(req,id):
    try:
        user = User.objects.get(id=id)
        return render(req,"users/show.html",{"user_show":user})
    except Exception as e:
        print(e)
        messages.error(req,"User not found")
        return redirect(reverse("dashboard:index"))

@login_required(login_url="index:signin")
def edit(req,id):
    user = User.objects.get(id=id)
    context = {
        "change_password": ChangePassword(user).as_p,
        "change_info": ChangeInfo().as_p,
    }
    req.session["id"] = id
    return render(req,"users/edit.html",context)

@login_required(login_url="index:signin")
def message(req,id):
    req = "will post a comment to " + str(id)
    return HttpResponse(req)

@login_required(login_url="index:signin")
def comment(req,user_id,comment_id):
    req = "will post a comment to user: " + str(user_id) + "on comment " + str(comment_id)
    return HttpResponse(req)
