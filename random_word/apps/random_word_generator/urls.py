from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^reset$',views.reset)
]
