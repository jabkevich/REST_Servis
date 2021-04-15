import decimal

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
import datetime

class User(AbstractUser):
    phone = models.CharField("phone", max_length=15, blank=True, null=False)
    first_name = models.CharField("first name", max_length=40, null=False)
    last_name = models.CharField("last name", max_length=40, null=False)
    patronymic = models.CharField("patronymic", max_length=40, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'patronymic']

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Wallet(models.Model):
    name = models.CharField('name', max_length=50)
    amount = models.DecimalField('Amount', default=0, max_digits=18, decimal_places=6)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def updateAmount(self, amount):
        self.amount = self.amount + amount
        self.save()

    def updateName(self, name):
        self.name = name
        self.save()

    def __str__(self):
        return self.name


class History(models.Model):
    TYPE = (
        ('debiting', 'debiting'),
        ('replenishment', 'replenishment')
    )
    data = models.DateTimeField('data', default=datetime.date.today)
    sum = models.DecimalField('sum', default=0, max_digits=18, decimal_places=6)
    wallet = models.ForeignKey(Wallet, on_delete=models.SET_NULL, null=True, related_name="wallet")
    typeOfTransaction = models.CharField(max_length=20, choices=TYPE)
    description = models.CharField(max_length=100, null=True) # имя карты или номер карты
