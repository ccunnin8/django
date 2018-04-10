from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..users.models import User
from models import Friendship
from django.db.models import Q
# Create your views here.
def index(req):
    if req.session["logged_in"]:
        user = User.objects.get(id=req.session["user_id"])
        context = {
            "friends": Friendship.objects.get_friends(user),
            "not_friends": Friendship.objects.get_rest(user)
        }
        return render(req,"friends/index.html", context )
    else:
        messages.error(req,"Please login!")
        return redirect(reverse("main:index"))

def friend(req,id):
    if req.session["logged_in"]:
        try:
            current_user_id = req.session["user_id"]
            current_user = User.objects.get(id=current_user_id)
            other_user = User.objects.get(id=id)
            Friendship.objects.create(current_user,other_user)
        except Exception as e:
            for error in e:
                messages.error(req,error)
        return redirect(reverse("friends:index"))
    else:
        messages.error(req,"Please login!")
        return redirect(reverse("main:index"))

def unfriend(req,id):
    if req.session["logged_in"]:
        try:
            current_user_id = req.session["user_id"]
            current_user = User.objects.get(id=current_user_id)
            other_user = User.objects.get(id=id)
            Friendship.objects.remove_friendship(current_user,other_user)
        except Exception as e:
            for error in e:
                messages.error(req,error)
        return redirect(reverse("friends:index"))
    else:
        messages.error(req,"Please login!")
        return redirect(reverse("main:index"))
