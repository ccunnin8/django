from django.shortcuts import render, HttpResponse, reverse, redirect
from django.contrib import messages
from models import User, Comment, Message
from forms import UserForm
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
    if req.session["admin"]:
        return render(req,"users/register.html")
    elif req.session["logged_in"]:
        messages.error(req,"You are not authorized to view this page")
        return render(reverse("dashboard:index"))
    else:
        messages.error(req,"You must log in!")
        return render(reverse("main:signin"))

def create(req):
    #check to see if password and password_conf are the same
    if req.POST["password"] != req.POST["password_conf"]:
        messages.error(req,"Your passwords do not match!")
        return redirect(reverse("index:register"))
    try:
        #make user object from model form
        new_user = UserForm(req.POST)
        user = new_user.save(commit=False)
        user.password = User.objects.encrypt_password(req.POST["password"])
        #if it's the first user make it an admin
        if len(User.objects.all()) == 0:
            user.admin = True
        user.save()
        #clear out form errors because it was a success!
        req.session["form_errors"] = []
        #redirect to the users page
        User.objects.login_user(req,user)
        return redirect(reverse("users:show",kwargs={"id": user.id}))
    except Exception as e:
        #show errors and redirect
        print(e)
        messages.error(req,"There was an error registering please try again")
        req.session["form_errors"] = new_user.errors
        return redirect(reverse("index:register"))

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

def destroy(req,id):
    #if the user being deleted is the user logged in OR the user is an admin delete, try to delete the user
    if req.session["user"]["id"] == id or req.session["admin"]:
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
