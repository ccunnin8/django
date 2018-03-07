from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(response):
    response =  "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(response):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(response):
    return redirect('/blogs')

def show(response,number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def edit(response,number):
    response = "placeholder to edit blog " + str(number)
    return HttpResponse(response)

def destroy(response,number):
    response = "placeholder to delete blog " + str(number)
    return HttpResponse(response)
