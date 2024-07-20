from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    rating = models.IntegerField()
    country = models.CharField(max_length=50)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    players = models.ManyToManyField(Player)

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ForeignKey(Player, related_name='player1_matches', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='player2_matches', on_delete=models.CASCADE)
    result = models.CharField(max_length=5, default='')  
    round_number = models.IntegerField()

