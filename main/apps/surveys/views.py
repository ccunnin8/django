from django.shortcuts import render, HttpResponse

# Create your views here.
def index(req):
    req = "placeholder to display all the surveys created"
    return HttpResponse(req)

def new(req):
    req = "placeholder for users to add a new survey"
    return HttpResponse(req)
