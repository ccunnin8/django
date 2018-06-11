from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^settings$',views.update_settings,name="update")
]
