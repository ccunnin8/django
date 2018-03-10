from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(req):
    return render(req,'session_words/index.html')

def add(req):
    date = strftime("%H:%M:%s %p %M-%d, %Y")
    word = req.POST["word"]
    color = req.POST["color"]
    if "big" in req.POST:
        big = req.POST["big"]
    else:
        big = False
    if "entries" in req.session:
        req.session["entries"].append({
            "date": date,
            "word": word,
            "color": color,
            "big": big
        })
    else:
        req.session["entries"] = []
    return redirect('/session_words')

def clear(req):
    req.session["entries"] = []
    return redirect('/session_words')
