from django.conf.urls import url

from . import views

app_label = "game"
urlpatterns = [
    url(r'^gameplay/$', views.gameplay, name="gameplay"),
    url(r'^names/$', views.names, name="names"),
    url(r'^packing/$', views.packing, name="packing"),
    url(r'^depart/$', views.depart, name="depart"),
    url(r'^play/$', views.play, name="play"),
    url(r'^win/$', views.win, name="win")
]

#What's the name for again?