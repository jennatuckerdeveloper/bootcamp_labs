from django.conf.urls import url

from . import views

app_label = "game"
urlpatterns = [
    url(r'^$', views.game, name="game")
]

