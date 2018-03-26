from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add$',views.add),
    url(r'^create$',views.create),
    url(r'^(?P<id>\d+)$',views.show),
    url(r'^add_review/(?P<id>\d+)$',views.add_review)
]
