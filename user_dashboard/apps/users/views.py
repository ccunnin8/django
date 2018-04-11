from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import User, Comment, Message
from django.contrib.auth import authenticate, login, get_user, user_login_failed
from django.contrib.auth.decorators import login_required
from forms import UserForm, ChangePassword, ChangeInfo
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

@login_required(login_url="index:signin")
def update(req):
    #get id in session from redirect and delete it
    id = req.session["id"]
    del req.session["id"]
    #if the id is the same as the person logged in then user =
    if get_user(req).id != id and get_user(req).is_staff:
        try:
            user = User.objects.get(id=id)
        except Exception as e:
            print(e)
            return redirect_admin_or_user(get_user(req).is_staff)
    elif get_user(req).id == id:
        user = get_user(req)
    else:
        return redirect(reverse("users:edit"))
    if user.id == id or get_user(req).is_staff:
        if req.POST["type"] == "password":
            #update passwor
            if req.POST["password"] != req.POST["password_conf"]:
                messages.error(req,"Your passwords do not match")
            else:
                if update_password(req,user):
                    return redirect_admin_or_user(user.is_staff)
        elif req.POST["type"] == "info":
            if update_info(req,user):
                return redirect_admin_or_user(user.is_staff)
        else:
            return None
        #everything failed!
    if get_user(req).is_staff:
        return redirect(reverse("users:edit_admin")
    else:
         return redirect(reverse("users:edit")

def update_password(req,user):
    new_user = ChangePassword(req.POST,instance=user)
    if new_user.is_valid():
        new_user.save()
        return True
    else:
        return False

def update_info(req,user):
    new_user = ChangeInfo(req.POST,instance=user)
    if new_user.is_valid():
        new_user.save()
        return True
    else:
        return False

def update_description(req,user,description_form):
    pass

def redirect_admin_or_user(admin):
    if admin:
        return redirect(reverse("dashboard:admin_dashboard"))
    else:
        return redirect(reverse("dashboard:index"))

@login_required(login_url="index:signin")
def show(req,id):
    try:
        user = User.objects.get(id=id)
        return render(req,"users/show.html",{"user_show":user})
    except Exception as e:
        messages.error(req,"User not found")
        if get_user(req).is_staff:
            return redirect(reverse("dashboard:admin_dashboard"))
        else:
            return redirect(reverse("dashboard:index"))

@login_required(login_url="index:signin")
def edit(req):
    return render(req,"users/edit.html", { "change_password": ChangePassword().as_p, "change_info": ChangeInfo().as_p})

@login_required(login_url="index:signin")
def edit_admin(req,id):
    context = {
        "change_password": ChangePassword().as_p,
        "change_info": ChangeInfo().as_p,
    }
    req.session["id"] = id
    return render(req,"users/edit_admin.html",context)

@login_required(login_url="index:signin")
def message(req,id):
    req = "will post a comment to " + str(id)
    return HttpResponse(req)

@login_required(login_url="index:signin")
def comment(req,user_id,comment_id):
    req = "will post a comment to user: " + str(user_id) + "on comment " + str(comment_id)
    return HttpResponse(req)
