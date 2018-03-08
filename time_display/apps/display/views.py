from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(req):
    context = {
        "date": strftime("%Y-%m-%d", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(req, 'display/index.html', context)
