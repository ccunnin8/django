from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index),
    url(r'^process_money',views.process_money)
]
