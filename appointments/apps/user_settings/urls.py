from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.update_settings,name="update")
]
