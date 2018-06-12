from models import Settings
from ..users.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import JsonResponse

def update_settings(req):
    user = User.objects.get(email=req.session["user"])
    try:
        settings = Settings.objects.update_or_create(
            email = req.POST["email"] == 'true',
            txt = req.POST["txt"] == 'true',
            phone_number = req.POST["phonenumber"],
            user = user
        )
        settings.full_clean()
        settings.save()
        return JsonResponse({"success": "settings updated" });
    except Exception as e:
        return JsonResponse({"failure": str(e) })
