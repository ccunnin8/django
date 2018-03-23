from django.conf.urls import url
import views

urlpatterns = [
    url(r'^admin$',views.admin,name="admin_dashboard"),
    url(r'^$',views.index,name="index")
]
