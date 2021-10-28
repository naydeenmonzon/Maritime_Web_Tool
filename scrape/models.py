import os
from datetime import datetime
from typing import Any
from django.conf.urls import static
from django.db import models
from django.utils.translation import gettext_lazy as _
import calendar


monthsNUM = [i for i in range(1,13)]
monthsNAME = [calendar.month_name[month_idx] for month_idx in range(1, 13)]
currentYear = datetime.now().year



MONTH_DICT = dict(zip(monthsNUM,monthsNAME))
MONTH_LIST = list(zip(monthsNUM,monthsNAME))

YEARS = [
    ('2021','2021'),('2020','2020')
]

CARRIER_LIST = [
        ('hlc','Hapag'),
        ('cma', 'CMA'),
        ('maeu', 'Maersk'),
        ('msc', 'MSC')
    ]




class Carrier(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    bool = models.BooleanField()
    def __str__(self,code,bool) -> str:
        return super().__str__(self,code, bool)

    def list():
        list = set(CARRIER_LIST)
        return list


# class BSFilter(models.Model):
#     carriers = models.CharField(max_length=20)
#     month = models.IntegerField()
#     year = models.IntegerField(choices=[(2020,'2020'),(2021,'2021')])
#     bool = models.BooleanField(blank=False,null=False)

#     MONTH_LIST = MONTH_LIST
#     def whatMonth(MONTH_LIST):
#         return MONTH_LIST.objects.all()
#     YEAR_CHOICES = ['2020','2021']
#     def whatyear(YEAR_CHOICES):
#         return YEAR_CHOICES.objects.all()


# class FourDigitYearConverter:
#     regex = '[0-9]{4}'
#     def to_python(self, value):
#         return int(value)
#     def to_url(self, value):
#         return '%04d' % value

