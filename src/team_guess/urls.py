from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("game/<int:riddle_id>/", views.game, name="game"),
]
