from django.conf.urls import url
from . import views

app_label = "home"
urlpatterns = [
    url(r'^$', views.home, name="home"),
]
