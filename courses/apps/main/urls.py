from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^courses/destroy/(?P<id>\d+)',views.destroy, name="destroy"),
    url(r'^create$',views.create, name="create"),
    url(r'^courses/comments/(?P<id>\d+)',views.comments, name="comments")
]
