from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    notes = models.TextField(default="no notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Books,related_name="authors")
