from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^createpost/$', views.createpost),
    url(r'^deletepost/(?P<post_id>[0-9]+)/', views.deletepost),
]
