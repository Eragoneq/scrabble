from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

urlpatterns = [
    path('', views.lobby, name='index'),
    path('game', views.game, name='game'),
]

urlpatterns += staticfiles_urlpatterns()
