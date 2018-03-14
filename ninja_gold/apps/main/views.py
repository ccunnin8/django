from django.shortcuts import render, HttpResponse, redirect
from random import randrange
import time
from datetime import datetime
# Create your views here.
def index(req):
    #initialize gold and status variables in session if not present
    if 'gold' not in req.session:
        req.session["gold"] = 0
        req.session["status"] = []
    return render(req,'main/index.html')

def process_money(req):
    ##SWITCH based on req.POST["loc"]
    if req.POST["loc"] == "farm":
        earned = randrange(10,21)
        req.session["gold"] += earned
    elif req.POST["loc"] == "cave":
        earned = randrange(5,11)
        req.session["gold"] += earned
    elif req.POST["loc"] == "house":
        earned = randrange(2,6)
        req.session["gold"] += earned
    elif req.POST["loc"] == "casino":
        earned = randrange(-50,51)
        req.session["gold"] += earned
    ##HANDLE ERRORS##
    else:
        earned = 0
        print("error occured")
        return redirect('/')
    ##GET TIME##
    ts = time.time()
    now = datetime.fromtimestamp(ts).strftime("%Y/%m/%d %I:%M %p")

    ##CONSTRUCT OUTPUT BASED ON RESULTS OF SWITCH##
    if earned > 0:
        output = "<p class='pos'>Earned " + str(earned) + " golds from the " + req.POST['loc'] +"! (" + now + ")</p>"
    else:
        output = "<p class='neg'>Entered a casino and lost {x} golds... Ouch. ({y})".format(x=earned,y=now)
    #append output to status#
    status = req.session["status"]
    status.append(output)
    req.session["status"] = status
    return redirect('/')
