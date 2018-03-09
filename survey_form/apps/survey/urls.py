from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^results$',views.results),
    url(r'^surveys/process$',views.process)
]
