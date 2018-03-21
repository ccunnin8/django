from django.shortcuts import render, HttpResponse, redirect, reverse
from django.forms import modelform_factory
from django.contrib import messages
from . import models
# Create your views here.
CourseForm = modelform_factory(models.Course, fields=("course_name",))
DescriptionForm = modelform_factory(models.Description,fields=("description",))
CommentForm = modelform_factory(models.Comments,fields=("comment",))
def index(req):
    return render(req,"main/index.html",
    {
        "CourseForm":CourseForm,
        "DescriptionForm":DescriptionForm,
        "courses": models.Course.objects.all()
    })

def destroy(req,id):
    try:
        course = models.Course.objects.get(id=id).delete()
        try:
            models.Description.objects.get(course_id=id).delete()
        except:
            messages.error(req,"Course had no description")
    except:
        messages.error(req,"Could not delete course")
    return redirect(reverse("index"))

def create(req):
    try:
        course = CourseForm(req.POST).save()
        desc = DescriptionForm(req.POST).save(commit=False)
        desc.course = course
        desc.save()
    except:
        messages.error(req,"Could Not Add Course")
    return redirect(reverse("index"))


def comments(req,id):
    course = models.Course.objects.get(id=id)
    comments = course.comments.all()
    if req.method == "POST":
        new_comment = CommentForm(req.POST).save(commit=False)
        new_comment.course = course
        new_comment.save()
    return render(req,"main/comments.html",
        {
        "comments":comments,
        "course": course,
        "CommentForm": CommentForm
        })

def new_comment(req):
    pass
