from mongoengine import *
from django.db import models
import datetime


class AccountInfo(models.Model):
    login = models.CharField(max_length=200)
    equity = models.CharField(max_length=200)
    balance = models.CharField(max_length=200)
    liabilities = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    leverage = models.CharField(max_length=200)
    #   server = StringField(max_length=200, required=True)

    def get_invested_capital(self):
        invested_capital = self.leverage * self.balance
        return invested_capital


class Deal(models.Model):
    account = models.ForeignKey(AccountInfo, on_delete=models.CASCADE)
    time = models.CharField(max_length=200)
    open = models.CharField(max_length=200)
    high = models.CharField(max_length=200)
    low = models.CharField(max_length=200)
    close = models.CharField(max_length=200)
    tick_volume = models.CharField(max_length=200)
    spread = models.CharField(max_length=200)
    real_volume = models.CharField(max_length=200)