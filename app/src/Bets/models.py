from django.db import models
from AUTH.models import Account
from Data.models import EventTeam


class Bet(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance = models.IntegerField()
    value = models.FloatField()
    canceled = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)


class SingleBet(Bet):
    team = models.ForeignKey(EventTeam, on_delete=models.CASCADE)
    multi = models.ForeignKey("MultiBet", on_delete=models.CASCADE,
                              verbose_name='bets')


class MultiBet(Bet):
    pass
