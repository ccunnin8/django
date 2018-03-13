from django.shortcuts import render, HttpResponse, redirect
from random import randint
# Create your views here.
def index(req):
    if "correct_num" not in req.session:
        req.session["correct_num"] = randint(1,100)
    print(req.session["correct_num"])
    return render(req,'main/index.html')

def guess(req):
    guess = int(req.POST["guess"])
    data = {
        "guess": guess,
        "correct": req.session["correct_num"]
    }
    if guess == req.session["correct_num"]:
        req.session["correct_num"] = randint(1,100)
    return render(req,'main/index.html',data)
