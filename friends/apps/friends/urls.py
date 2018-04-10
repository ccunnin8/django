from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^friend/(?P<id>\d+)$',views.friend,name="friend"),
    url(r'^unfriend/(?P<id>\d+)$',views.unfriend,name="unfriend")
]
