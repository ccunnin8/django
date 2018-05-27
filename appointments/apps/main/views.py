from django.shortcuts import render, reverse, redirect
from ..users.models import User, UserForm
from django.contrib import messages

# Create your views here.
def index(req):
    user_form = UserForm()
    return render(req,"main/index.html", {"user_form" : user_form.as_p });

def login(req):
    #try to get the user with that email
    try:
        user = User.objects.get(email=req.POST["email"])
    except:
        messages.error(req,"User not found!")
        return redirect(reverse("main:index"))
    #check if the password is right
    if User.objects.check_password(req.POST["password"],user.password):
        User.objects.login(req.session,user)
        return redirect(reverse("appointments:index"))
    else:
        messages.error(req,"That password was not correct!")
        return redirect(reverse("main:index"))


def logout(req):
    User.objects.logout(req.session)
    return redirect(reverse("main:index"))

def register(req):
    #GET FORM
    user = UserForm(req.POST)
    #PASSWORDS MATCH?
    if req.POST["password"] != req.POST["password_confirmation"]:
        messages.error(req,"Your passwords do not match!")
        return redirect(reverse("main:index"))

    #CHECK IF DATA IS VALID?
    print(user.is_valid(req.POST["birthdate"]))
    if user.is_valid(req.POST["birthdate"]):
        new_user = User.objects.create(
            name=req.POST["name"],
            email=req.POST["email"],
            password=User.objects.encrypt_password(req.POST["password"]),
            birthdate=User.objects.valid_date_format(req.POST["birthdate"])
        )
        User.objects.login(req.session,new_user)
        return redirect(reverse("appointments:index"))
    else:
        messages.error(req,user.errors)
        return redirect(reverse("main:index"))
