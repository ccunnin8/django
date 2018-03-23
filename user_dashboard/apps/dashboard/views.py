from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,"dashboard/index.html")

def admin(req):
    return render(req,"dashboard/dashboard_admin.html")
