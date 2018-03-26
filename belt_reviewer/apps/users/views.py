from django.shortcuts import render
from django.contrib import messages
from ..users.models import User
# Create your views here.
def index(req,id):
    try:
        user = User.objects.get(id=id)
        reviews = user.reviews.all()
        total_reviews = len(reviews)
        return render(req,"users/index.html",{"user":user, "reviews": reviews, "total": total_reviews})
    except:
        messages.error(req,"Something went wrong")
        return render("/books")
