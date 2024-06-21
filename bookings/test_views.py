from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import BookingForm
from .models import Booking

# Create your tests here.

# class TestDjango(TestCase):

#     def test_this_thing_works(self):
#         self.assertEqual(1, 1)


class TestBookingsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Jimmy",
            email="test@test.com",
            password="myPassword"         
        )
        self.booking = Booking(
            username=self.user,
            date="2024-07-04",
            sheet_time="Sheet 1 at 18:00",
	        wheelchair_sheet="Required"
        )
        self.booking.save()

    def test_render_booking_list_with_form(self):
        response = self.client.get(reverse('bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, response.content)
        self.assertIn("2024-07-04", response.content)
        self.assertIn(b"Sheet 1 at 18:00", response.content)
        self.assertIn(b"Required", response.content)
        self.assertIsInstance(response.context['booking_form'], BookingForm)


