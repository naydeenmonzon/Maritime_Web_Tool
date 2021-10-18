import os

from datetime import datetime
from typing import Any
from django.conf.urls import static
from django.db import models

from django.utils.translation import gettext_lazy as _
import calendar




class Filters(models.Model):
    C = 'Carrier'
    MF = 'Month From'
    MT = 'Month To'
    Y = 'Year'
    FILTER_CHOICE = (
        ('C','Carrier'),
        ('MF','Month From'),
        ('MT', 'Month To'),
        ('Y','Year')
    )
    filter_choice = models.CharField(
        max_length=2,
        blank=False,
        choices=FILTER_CHOICE
        )
    
    def CarrierFilter(self):
        return self.filter_choice in {
            self.FILTER_CHOICE['C']
        }
    def YearFilter(self):
        return self.filter_choice in {
            self.FILTER_CHOICE['Y']
        }
    def MFfilter(self):
        return self.filter_choice in {
            self.FILTER_CHOICE['MF']
        }
    def MTfilter(self):
        return self.filter_choice in {
            self.FILTER_CHOICE['MT']
        }

print(Filters.FILTER_CHOICE)


class Carriers(models.Model):
    code = models.CharField(max_length=3,primary_key=True)
    name = models.CharField(max_length=100)


    @classmethod
    def  create(cls, code, name):
        carrier = cls(
            code = code,
            name = name,
        ).save()
        return carrier
    def dict(self, code):
        dict = __dict__[
            self: self,
            code: code,
        ]
        return dict



class Years(models.Model):
    year = models.IntegerField( )


    @classmethod
    def create(cls,year):
        year = cls(
            year = year,
        ).save()
        return year




class Month(models.Model):
    name = models.CharField(max_length=20 )
    value = models.IntegerField()
    

    class Meta:
        abstract = True

    @classmethod
    def create(cls, name, value:int):
        month = cls(
            name = name,
            value = value,
        ).save()
        return month
    
    

class MonthFrom(Month):

    def __init__(self, name, value:int):
        super().__init__(self, name, value)
    def __getstate__(self) -> dict:
        return super().__getstate__()



class MonthTo(Month):

    def __init__(self, name, value:int):
        super().__init__(self,name, value)
    def __getstate__(self) -> dict:
        return super().__getstate__()




currentMonth = datetime.now().month
currentYear = datetime.now().year

monthsNUM = [currentMonth for currentMonth in range(1,13)]
monthsNAME = [calendar.month_name[month_idx] for month_idx in range(1, 13)]

monthLIST = list(zip(monthsNAME,monthsNUM))
monthDICT = dict(zip(monthsNUM,monthsNAME))

#Carriers.create('hlc','Hapag-Lloyd')
#Carriers.create('cma', 'CMA')
#Carriers.create('maeu', 'Maersk')
#Carriers.create('msc', 'MSC')


#Years.create(2020)
#Years.create(2021)


#MonthFrom(monthsNAME,monthsNUM)
#MonthTo(monthsNAME,monthsNUM)