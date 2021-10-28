
from datetime import datetime
from django.template.loader import render_to_string
from django import forms
from django.db import models
from django.db.models.aggregates import Variance
from django.db.models.lookups import Range, YearLte
from django.forms import fields, widgets
from django.forms.models import model_to_dict
from django.utils.regex_helper import contains
from django.utils.translation import activate, gettext_lazy as _
from datetime import date
from django.forms.widgets import HiddenInput, Widget

from .models import CARRIER_LIST, YEARS, MONTH_LIST, MONTH_DICT





class BSfilterForm(forms.Form):

    carriers = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class':"form-check-input",
            'type':"checkbox",
            'role':"switch",}),
        choices=CARRIER_LIST,
        label= 'Carriers',)

    monthF = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(
            attrs={'class':'slider','type':'range','id':'MonthFrom',}))

    monthT = forms.IntegerField(
        required=True,
        min_value=1,
        max_value=12,
        widget=forms.NumberInput(attrs={'class':'slider','type':'range','id':'MonthTo',}))
        
    year = forms.MultipleChoiceField(
        required=True,
        choices=YEARS,
        widget=forms.CheckboxSelectMultiple(attrs={
            'type':'checkbox','class':'btn-check', 'name':'yearOptions','autocomplete':'on'
        }),
    )
    



