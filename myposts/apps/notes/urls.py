from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add_note$',views.add_note),
    url(r'^update_note/(?P<id>\d+)$',views.update_note),
    url(r'^delete_note/(?P<id>\d+)$',views.delete_note)
]
