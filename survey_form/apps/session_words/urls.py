from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add_word$',views.add),
    url(r'^clear$',views.clear)
]
