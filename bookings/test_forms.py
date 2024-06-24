from django.test import TestCase
from django.urls import reverse
from .forms import BookingForm

# Create your tests here.


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        booking_form = BookingForm(
            {"date": "2024-07-22",
             "sheet_time": "Anytime",
             "wheelchair_sheet": "Yes"
             }
        )
    self.assertTrue(booking_form.is_valid())
