from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^new$',views.new,name="new"),
    url(r'^<int:id>$',views.show, name="show"),
    url(r'^$',views.index,name="index"),
    url(r'^<int:id>/edit$',views.edit,name="edit"),
    url(r'^create$',views.create,name="create"),
    url(r'^<int:id>/destroy$',views.destroy,name="destroy"),
    url(r'^update$',views.update,name="update")
]
