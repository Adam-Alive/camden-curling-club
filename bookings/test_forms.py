from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import BookingForm

# Create your tests here.


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 0)


class TestBookingForm(TestCase): 
 
    def test_form_is_valid(self): 
        booking_form = BookingForm(
            {'date': '04/04/2024',
             'sheet_time': 'Test 10:00',
             'wheelchair_sheet': 'Required'

        }
        ) 
        self.assertTrue(booking_form.is_valid())