from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search$',views.filter_users),
    url(r'^search/(?P<id>\d+)$',views.filter_users),
    url(r'^(?P<id>\d+)$',views.index),
    url(r'^$',views.index)
]
