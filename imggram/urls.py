from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="imggram_index"),
    url(r'^show/(?P<post_id>[0-9]+)/$', views.show),
    url(r'^upload/$', views.upload),
    url(r'^like/$', views.like_it),
]
