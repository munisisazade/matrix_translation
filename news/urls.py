from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home, name="index"),
    url(r'^about/$', views.about, name="about"),
]
