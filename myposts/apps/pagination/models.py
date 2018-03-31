from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def how_many_pages(self,total,default):
        if total % default != 0:
            return (total / default) + 1
        else:
            return total / default

    def get_start_end(self,id,pagination_factor):
        if id == 1:
            start = 0
            end = pagination_factor
        else:
            end = id * pagination_factor
            start = end-pagination_factor
        return (start,end)
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    objects = UserManager()
