from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new$',views.new,name="new"),
    url(r'^(?P<id>\d+)$',views.show, name="show"),
    url(r'^$',views.index,name="index"),
    url(r'^(?P<id>\d+)/edit$',views.edit,name="edit"),
    url(r'^create$',views.create,name="create"),
    url(r'^(?P<id>\d+)/destroy$',views.destroy,name="destroy"),
    url(r'^update$',views.update,name="update")
]
