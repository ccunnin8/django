from models import Settings
from ..users.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import JsonResponse
def update_settings(req):
    user = User.objects.get(email=req.session["user"])
    settings = Settings.objects.create(req.POST)
    settings.user = user
    if settings.validate():
        settings.save()
    else:
        messages.error(req,"There was an error saving settings")
        return redirect(reverse("appointments:index"))
    return JsonResponse({"success": "settings updated" });
