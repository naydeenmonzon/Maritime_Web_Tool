from django import forms
from django.forms.widgets import Select



MONTHdata = {
    {"month":"January",
        "id":1
    },
    {"month":"February",
        "id":2
    },
    {"month":"March",
        "id":3
    },
    {"month":"April",
        "id":4
    },
    {"month":"May",
        "id":5
    },
    {"month":"June",
        "id":6
    },
    {"month":"July",
        "id":7
    },
    {"month":"August",
        "id":8
    },
    {"month":"September",
        "id":9
    },
    {"month":"October",
        "id":10
    },
    {"month":"November",
        "id":11
    },
    {"month":"December",
        "id":12
    }
}



class Carriers(forms.Forms):
    name = forms.CharField(max_length=50)
    pass

class YearFilter(forms.forms):
    name = forms.IntegerField()

    class BooleanField():
        
        pass

class MonthFilter(forms.Form):
    monthName = forms.CharField(max_length=50)
    pass

class DateFrom(MonthFilter):
    name = forms.DateInput

def NullBooleanField(
    widget=Select(
        choices=[
            ('', 'Unknown'),
            (True, 'Yes'),
            (False, 'No'),
        ]
    )
)