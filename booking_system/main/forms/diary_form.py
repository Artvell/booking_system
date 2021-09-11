from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'id': 'datepicker'})

class DiaryForm(forms.Form):
    CHOICES=[
        (1,'1'),
        (3,'3'),
        (7,"7"),
        (31,"31")
    ]

    days = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect,required=True, initial=1)
    start_date = forms.DateField(widget=DateInput(),required=True)