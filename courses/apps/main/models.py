from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=255,validators=[MinLengthValidator(5)])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
#A course has 1 description
class Description(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(Course, related_name="description")
#A course can have many comments
class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.ForeignKey(Course,related_name="comments")
