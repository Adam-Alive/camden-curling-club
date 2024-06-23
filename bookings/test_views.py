from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking
from .forms import BookingForm

# Create your tests here.


class TestBookingsViews(TestCase):
    """
    Test views from the views.py file.
    """

    def setUp(self):
        """
        Set up test user and booking
        to test CRUD functionality.
        """
        self.user = User.objects.create_user(
            username="Jimmy",     
            password="myPassword"     
        )

        self.booking = Booking(
            username=self.user,       
            date="2024-07-04",
            sheet_time="Anytime",
	        wheelchair_sheet="Yes"
        )
        self.booking.save()

    def test_render_bookings_page(self):
        response = self.client.get(reverse('bookings'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_list.html')

    
    def test_render_make_booking_page(self):
        response = self.client.get(reverse('make_booking'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_render_my_bookings_page(self):
        response = self.client.get(reverse('my_bookings'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')

    def test_render_edit_bookings(self):
        response = self.client.get(reverse('edit_booking'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)

    def test_successful_make_booking_by_user(self):
        response = self.client.get(reverse('make_booking'))
        # print(response.content)
        self.assertIn(b"Jimmy", response.content)
        self.assertIn(b"2024-07-04", response.content)
        self.assertIn(b"Anytime", response.content)
        self.assertIn(b"Yes", response.content)
        self.assertIsInstance(response.context['booking_form'], BookingForm)


