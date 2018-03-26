from django.shortcuts import render, redirect
from django.contrib import messages
from models import Book, Review, Author
from ..users.models import User
# Create your views here.
def index(req):
    context = {
        "user": User.objects.get(id=req.session["user_id"]),
        "books": Book.objects.all(),
        "reviews": Review.objects.all()[:3]
    }
    return render(req,"books/index.html",context)

def add(req):
    context = {
        "authors": Author.objects.all()
    }
    return render(req,"books/add_book.html",context)

def create(req):
    try:
        Book.objects.validate(req.POST)
        Review.objects.validate(req.POST)
    except Exception as e:
        print(e)
        messages.error(req,e[0])
        return redirect("/books/add")
    try:
        book = Book.objects.create_book(req.POST)
        user = User.objects.get(id=req.session["user_id"])
        Review.objects.create_review(book,user,req.POST)
        return redirect("/books")
    except Exception as e:
        print(e)
        messages.error(req,"Something went wrong")
        return redirect("/books/add")

def show(req,id):
    try:
        book = Book.objects.get(id=id)
        reviews = book.reviews.all()
        return render(req,"books/show_book.html",{"book":book, "reviews": reviews })
    except Exception as e:
        print(e)
        messages.error(req,"Book not found!")
        return redirect("/books")

def add_review(req,id):
    try:
        book = Book.objects.get(id=id)
        user = User.objects.get(id=req.session["user_id"])
        Review.objects.create_review(book,user,req.POST)
    except Exception as e:
        print(e)
        messages.error(req,"Something went wrong")
    return redirect("/books/" + str(id))
