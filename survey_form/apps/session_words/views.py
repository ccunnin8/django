from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(req):
    if "entries" not in req.session:
        req.session["entries"] = []
    print req.session["entries"]
    return render(req,'session_words/index.html')

def add(req):
    date = strftime("%r:%M:%S %p %b %d, %Y")
    try:
        word = req.POST["word"]
        color = req.POST["color"]
    except:
        print "ERROR must choose color and word"
        return redirect('/session_words')

    if "big" in req.POST:
        big = req.POST["big"]
    else:
        big = False
    if "entries" in req.session:
        entries = req.session["entries"]
        entries.append({
            "date": date,
            "word": word,
            "color": color,
            "big": big
        })
        req.session["entries"] = entries
    else:
        print "error occured"
        return redirect('/session_words')
    print req.session["entries"]
    return redirect('/session_words')

def clear(req):
    req.session["entries"] = []
    return redirect('/session_words')
