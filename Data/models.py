from django.db import models
from django.utils import timezone


class Bookmaker(models.Model):
    def __str__(self):
        return f"Bookmaker#{self.id}"

    base_url = models.URLField()
    name = models.CharField(max_length=20, default=__str__)
    active = models.BooleanField(default=True)
    created_date = models.DateField(default=timezone.now)


class InfoSponsor(models.Model):
    base_url = models.URLField()


class Team(models.Model):
    added_date = models.DateField(default=timezone.now)


class TeamName(models.Model):
    name = models.CharField(max_length=40)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='names')


class Category(models.Model):
    name = models.CharField(max_length=20)
    bookmaker = models.ForeignKey(
        Bookmaker, on_delete=models.CASCADE, default=0)
    main_category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                      related_name='subcategories')


class Event(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Game(models.Model):
    STATUS_CHOICES = [
        (0, "Created"),
        (1, "Sponsor search"),
        (2, "Waiting for the start"),
        (3, "Started"),
        (4, "Ended"),
        (5, "Waiting"),
        (6, "Canceled"),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    sponsor = models.ForeignKey(InfoSponsor, on_delete=models.CASCADE)
    sponsor_url = models.URLField()
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    bookmaker_url = models.URLField()
    start_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)


class EventTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name="teams")


class EventTeamBet(models.Model):
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    team = models.ForeignKey(EventTeam, on_delete=models.CASCADE)
    value = models.FloatField()
