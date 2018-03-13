from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^guess$',views.guess),
    url(r'^$',views.index)
]
