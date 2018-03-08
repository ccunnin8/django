from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string
from string import ascii_lowercase
# Create your views here.
def index(req):
    if "counter" in req.session:
        req.session["counter"] += 1
    else:
        req.session["counter"] = 1
    random_word = get_random_string(length=14,allowed_chars=ascii_lowercase)
    context = {
        "random_word": random_word
    }
    return render(req, 'random_word_generator/index.html',context)

def reset(req):
    req.session["counter"] = 0
    return redirect('/random_word')
