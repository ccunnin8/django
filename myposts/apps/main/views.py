from django.shortcuts import render, HttpResponse
from models import Post
# Create your views here.
def index(req):
    context = {
        "posts": Post.objects.all()
    }
    return render(req,"main/index.html", context)

def add_post(req):
    post_text = req.POST["new_post"]
    post = Post.objects.create(post=post_text)
    return render(req,"main/post.html",{"post": post})
