from django.shortcuts import render, HttpResponse, redirect
from django.utils.timezone import make_aware
from django.core import serializers
from models import User
from django.db.models import Q
from datetime import datetime
# Create your views here.
pagination_factor = 5


def index(req,id=1):
    id = int(id)
    start,end = User.objects.get_start_end(id,pagination_factor)
    total = len(User.objects.all())
    pages = User.objects.how_many_pages(total,pagination_factor)
    context = {
        "users" : User.objects.all().order_by("id")[start:end],
        "pages" : [num + 1 for num in range(pages)]
    }
    return render(req,"pagination/index.html", context)

def filter_users(req,id=1):
    dateformat = "%m/%d/%Y"
    name = req.GET.get('name')
    #get startend
    id = int(id)
    start,end = User.objects.get_start_end(id,pagination_factor)
    #go back to beginning if everything blank
    ##SUPER UGLY CODE THAT NEEDS TO BE CLEANED UP AND OPTIMIZED!!!!
    if name == "" and req.GET["to"] == "" and req.GET["from"] == "":
        users = User.objects.all()
        total = len(users)
        pages = User.objects.how_many_pages(total,pagination_factor)
        return render(req,"pagination/search_users.html",{"users":users[start:end], "pages": [num + 1 for num in range(pages)]})

    if name != "":
        users = User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))

    else:
        users = User.objects.all()

    if req.GET.get("to") != "" and req.GET.get("from") !="":
        try:
            to_date = make_aware(datetime.strptime(req.GET["to"],dateformat))
            from_date = make_aware(datetime.strptime(req.GET["from"],dateformat))
            users = users.filter(created_at__range=[from_date,to_date])
        except Exception as e:
            print(e)
    total = len(users)
    ###END CODE THAT IS SUPER UGLY AND NEEDS TO BE REFACTORED!!!######
    pages = User.objects.how_many_pages(total,pagination_factor)
    context = {"users": users[start:end], "pages": [num + 1 for num in range(pages)]}
    return render(req,"pagination/search_users.html",context)
