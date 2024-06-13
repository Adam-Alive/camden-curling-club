from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    A widget to display a datepicker for the user
    when making a booking.
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    Connects the Booking model to the form
    and will populate the data fields when the
    user submits a booking.
    """
    class Meta:
        model = Booking
        fields = ('date', 'sheet_time', 'wheelchair_sheet',)
        widgets = {
            'date': DateInput(),
        }
