from django.db import models
from django.utils import timezone
from django.core.validators import *

class Team(models.Model):
    date = models.DateField(
        default=timezone.now)
    publishedDate = models.DateTimeField(
        default=timezone.now)
    score = models.IntegerField(
		default=0)
    scoreList = models.CharField(
        max_length=500,
        validators=[validate_comma_separated_integer_list],
		null=True,
    )
    associatedTags = models.TextField(
		default='')
    name = models.CharField(
        max_length = 5)
    longName = models.CharField(
        max_length = 30,
		null=True,
	)
    homeColour = models.CharField(
		max_length = 6,
		null=True,
	)
    awayColour = models.CharField(
		max_length = 6,
		null=True,
	)
    league = models.CharField(
        max_length = 30,
		default='Premier League',
	)
    nextGame = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
        null=True,
    )
    imagePath = models.CharField(
        max_length = 50,
        null=True,
	)
    def __str__(self):
        return self.longName
    
class Player(models.Model):
    firstName = models.CharField(
        max_length=50,
        null=True)
    lastName = models.CharField(
        max_length=50)
    score = models.IntegerField(
		default=0)
    lastScore = models.IntegerField(
		default=0)
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
		null=True,
    )
    def __str__(self):
        return self.lastName
