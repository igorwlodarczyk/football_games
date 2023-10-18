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
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    season = models.CharField(max_length=200)
    formation = models.CharField(max_length=200)
    enemy_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    result = models.CharField(max_length=200)
    player_1 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_2 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_3 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_4 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_5 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_6 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_7 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_8 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_9 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_10 = models.ForeignKey(Country, on_delete=models.CASCADE)
    player_11 = models.ForeignKey(Country, on_delete=models.CASCADE)
