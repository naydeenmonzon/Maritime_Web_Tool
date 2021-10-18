from django import forms
from datetime import datetime
import calendar



currentMonth = datetime.now().month
currentYear = datetime.now().year

monthsNUM = [currentMonth for currentMonth in range(1,13)]
monthsNAME = [calendar.month_name[month_idx] for month_idx in range(1, 13)]

MONTH_LIST = list(zip(monthsNUM,monthsNAME))
MONTH_DICT = dict(zip(monthsNUM,monthsNAME))
CARRIER_LIST = [
    ('hlc','Hapag-Lloyd'),
    ('cma', 'CMA'),
    ('maeu', 'Maersk'),
    ('msc', 'MSC')
]
YEAR_CHOICES = ['2020','2021']

data = {
    'carrier':'hlc',
    'year':'2021',
    'montFrom':currentMonth,
    'monthTo':currentMonth,
}

class DashboardFilter(forms.Form):
    carrier = forms.MultipleChoiceField(
        label='carrierList',
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=CARRIER_LIST
    )
    year = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=YEAR_CHOICES
    )
    monthFrom = forms.ChoiceField(
        required=False,
        widget = forms.Select,
        choices=MONTH_LIST
    )
    monthTo = forms.ChoiceField(
        required=False,
        widget = forms.Select,
        choices=MONTH_LIST
    )
print(DashboardFilter)