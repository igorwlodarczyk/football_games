from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=200)
    flag = models.ImageField(upload_to="files/flags")


class Club(models.Model):
    name = models.CharField(max_length=255)
    league = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Riddle(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="club")
    season = models.CharField(max_length=200)
    formation = models.CharField(max_length=200)
    enemy_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="enemy_club")
    result = models.CharField(max_length=200)
    player_1 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_1")
    player_2 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_2")
    player_3 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_3")
    player_4 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_4")
    player_5 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_5")
    player_6 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_6")
    player_7 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_7")
    player_8 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_8")
    player_9 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_9")
    player_10 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_10")
    player_11 = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="player_11")
