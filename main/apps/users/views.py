from django.shortcuts import render, HttpResponse

# Create your views here.
def register(req):
    req = "placeholder for users to create a new user record"
    return HttpResponse(req)

def login(req):
    req = "placeholder for users to login"
    return HttpResponse(req)

def index(req):
    req = "index"
    return HttpResponse(req)
