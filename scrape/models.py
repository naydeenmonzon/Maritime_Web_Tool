from enum import auto
import os
from datetime import datetime
from typing import Iterable
from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.db import models
from django.db.models import indexes
from django.db.models import fields
from django.db.models.fields import Field
from django.template.context import make_context
from django.utils.translation import gettext_lazy as _
import calendar
from django.template import Context


#from scrape.views import blanksailing, vesselroute
#from django.db.models.enums import Choices

currentMonth = datetime.now().month
currentYear = datetime.now().year


monthsNUM = [currentMonth for currentMonth in range(1,13)]
monthsNAME = [calendar.month_name[month_idx] for month_idx in range(1, 13)]

monthLIST = list(zip(monthsNAME,monthsNUM))
monthDICT = dict(zip(monthsNUM,monthsNAME))

class TOOLS(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    urlNAME = models.CharField(max_length=50)
    def __init__(self, *args, **kwargs) -> None:
        super(TOOLS, self).__init__(*args, **kwargs)
    def __str__(self):
        return (self.urlNAME, self.name)

    @admin.display(boolean=True)
    def test(self):
        return self.urlNAME

    class Meta:
        indexes = [
            models.Index(fields=['urlNAME'], name='urlNAME_idx')
        ]



