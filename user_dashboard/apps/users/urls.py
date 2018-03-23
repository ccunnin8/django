from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^new$',views.new,name="new"),
    url(r'^create$',views.create,name="create"),
    url(r'^remove/(?P<id>\d+)$',views.destroy,name="remove"),
    url(r'^edit$',views.edit,name="edit"),
    url(r'^edit/(?P<id>\d+)$',views.edit_admin,name="edit_admin"),
    url(r'^show/(?P<id>\d+)$',views.show,name="show"),
    url(r'^update/(?P<id>)',views.update,name="update"),
    url(r'^message/(?P<id>)',views.message,name="message"),
    url(r'^comment/(?P<user_id>)/(?P<comment_id>)',views.comment,name="comment")
]
