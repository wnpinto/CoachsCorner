from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)

    @receiver(post_save, sender=User)
    def save_player(sender, instance, created, **kwargs):
        user = instance
        if created:
            player = Player()
            player.user = user
            player.age = 0
            player.sex = 'X'
            player.save()


class Sport(models.Model):
    name = models.CharField(max_length=50, blank=False)


class Team(models.Model):
    name = models.CharField(max_length=50, blank=False)
    sport_id = models.ForeignKey(Sport, "sport_id", default=None)
    slogan = models.CharField(max_length=30, default=None, null=True)
    rating = models.DecimalField(default=3.00, decimal_places=2, max_digits=3)


class TeamMember(models.Model):
    player_id = models.ForeignKey(Player, "player_id", default=None)
    team_id = models.ForeignKey(Team, "team_id", default=None)
    player_number = models.IntegerField(default=None, null=True)


class TeamColour(models.Model):
    team_id = models.ForeignKey(Team, "team_id", default=None)
    primary = models.CharField(default="FFFFFF", max_length=6, blank=False, null=True)
    secondary = models.CharField(default="FFFFFF", max_length=6, blank=False, null=True)
    tertiary = models.CharField(default="FFFFFF", max_length=6, blank=False, null=True)
