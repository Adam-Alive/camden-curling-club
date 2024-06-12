from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'sheet_time', 'wheelchair_sheet',)
        widgets = {
            'date': DateInput(),
        }
