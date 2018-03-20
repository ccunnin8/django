from django.shortcuts import render, HttpResponse

# Create your views here.
def edit(req):
    req = "placeholder for users to create a new user record"
    return HttpResponse(req)

def show(req):
    req = "placeholder for users to login"
    return HttpResponse(req)

def create(req):
    pass

def destroy(req):
    pass

def update(req):
    pass
    
def index(req):
    req = "index"
    return HttpResponse(req)
