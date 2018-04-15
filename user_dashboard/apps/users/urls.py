from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^new$',views.new,name="new"),
    url(r'^create$',views.create,name="create"),
    url(r'^remove/(?P<id>\d+)$',views.destroy,name="remove"),
    url(r'^edit/(?P<id>\d+)$',views.edit,name="edit"),
    url(r'^show/(?P<id>\d+)$',views.show,name="show"),
    url(r'^update$',views.update,name="update"),
    url(r'^message$',views.message,name="message"),
    url(r'^comment$',views.comment,name="comment")
]
