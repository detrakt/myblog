from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth/$', views.auth),
    url(r'^error/$', views.error),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
]
