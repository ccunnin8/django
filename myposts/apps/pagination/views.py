from django.shortcuts import render, HttpResponse
from models import User
from django.db.models import Q
from datetime import datetime
# Create your views here.
pagination_factor = 4


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
    start, end = User.objects.get_start_end(int(id),pagination_factor)
    dateformat = "%m/%d/%Y"
    name = req.GET.get('name')
    id = int(id)
    start,end = User.objects.get_start_end(id,pagination_factor)

    if name != "":
        users = User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))
    else:
        users = User.objects.all()
    if req.GET.get("to") != "" and req.GET.get("from") !="":
        try:
            to_date = datetime.strptime(req.GET["to"],dateformat)
            from_date = datetime.strptime(req.GET["from"],dateformat)
            users.exclude(Q(created_at__lte=from_date) | Q(created_at__gte=to_date))
        except Exception as e:
            print(e)
    total = len(users)
    pages = User.objects.how_many_pages(total,pagination_factor)
    if pages < pagination_factor:
        pages = None
    else:
        pages = [num + 1 for num in range(pages)]
    context = {
        "users": users,
        # "pages": pages
    }
    return render(req,"pagination/index.html",context)
