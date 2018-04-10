from __future__ import unicode_literals
from ..users.models import User
from django.db import models
from django.db.models import Q

class FriendshipManager(models.Manager):
    def remove_friendship(self,user1,user2):
        self.filter(user=user1).filter(friend=user2).delete()
        self.filter(user=user2).filter(friend=user1).delete()

    def create(self,user1,user2):
        super(FriendshipManager,self).create(user=user1,friend=user2)
        super(FriendshipManager,self).create(user=user2,friend=user1)

    def get_friends(self,user1):
        return [user.user for user in User.objects.get(id=user1.id).friends.all()]

    def get_rest(self,user1):
        return User.objects.all().exclude(friends__in=self.filter(user=user1)).exclude(id=user1.id)
# Create your models here.
class Friendship(models.Model):
    user = models.ForeignKey(User,default=None)
    friend = models.ForeignKey(User,related_name="friends",default=None)
    objects = FriendshipManager()
