from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.TextField()
