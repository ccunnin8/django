from django.shortcuts import render, redirect, HttpResponse
from models import Note
# Create your views here.
def index(req):
    context = { "notes": Note.objects.all() }
    return render(req,"notes/index.html", context )

def add_note(req):
    title = req.POST["title"]
    note = Note.objects.create(title=title)
    return render(req,"notes/notes.html",{"note": note})

def update_note(req,id):
    note = Note.objects.get(id=id)
    note.description = req.POST["description"]
    note.save()
    return HttpResponse("changed")

def delete_note(req,id):
    Note.objects.get(id=id).delete()
    return redirect("/notes")
