from django.conf.urls import include, url  
from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^connect/?$', views.connect, name="connect"),
    url(r'^inscript/?$', views.inscript, name="inscript")
]