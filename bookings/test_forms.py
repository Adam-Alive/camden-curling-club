from django.test import TestCase
from django.urls import reverse
from .forms import BookingForm

# Create your tests here.


class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        booking_form = BookingForm(
            {"date": "2024-07-22",
             "sheet_time": "Sheet 3 at 18.00 - 19.30",
             "wheelchair_sheet": "Required"
             }
        )
        self.assertTrue(booking_form.is_valid())

    def test_form_is_invalid(self):
        booking_form = BookingForm(
            {"date": "2024-07-22",
             "sheet_time": "Sheet x",
             "wheelchair_sheet": " "
             }
        )
        self.assertFalse(booking_form.is_valid())
