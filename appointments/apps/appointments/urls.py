from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^add$',views.add,name="add"),
    url(r'^edit/(?P<id>\d+)$',views.edit,name="edit"),
    url(r'^delete/(?P<id>\d+)$',views.delete,name="delete"),
    url(r'^update$',views.update,name="update")
]
