from django.shortcuts import render, get_object_or_404
from .models import Riddle, Club

# Create your views here.


def index(request):
    return render(request, "team_guess/index.html")


def game(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    all_clubs = Club.objects.all()
    return render(
        request, "team_guess/index.html", {"riddle": riddle, "clubs": all_clubs}
    )
