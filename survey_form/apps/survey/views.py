from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    return render(req, "survey/index.html")

def results(req):
    return render(req,'survey/result.html')

def process(req):
    if "counter" in req.session:
        req.session["counter"] += 1
    else:
        req.session["counter"] = 1
    req.session["name"] = req.POST["name"]
    req.session["location"] = req.POST["location"]
    req.session["lang"] = req.POST["fav_lang"]
    req.session["comment"] = req.POST["comment"]
    return redirect('/results')
