import datetime
import random
from django.shortcuts import render, get_object_or_404, redirect
from decouple import config
from .models import Riddle, Club


def calculate_game_day():
    deployment_date = datetime.datetime.strptime(config("DEPLOYMENT_DATE"), "%Y-%m-%d")
    today = datetime.datetime.now()
    game_day = (today - deployment_date).days
    return game_day + 1


def index(request):
    game_day = calculate_game_day()
    return redirect("game", riddle_id=game_day)


def game(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    all_clubs = Club.objects.all()
    random_day = random.randint(1, calculate_game_day())
    return render(
        request,
        "team_guess/index.html",
        {"riddle": riddle, "clubs": all_clubs, "random_day": random_day},
    )
