from django.conf.urls import url
import views

urlpatterns = [
    url(r'^admin$',views.index),
    url(r'^$',views.index,name="index")
]
