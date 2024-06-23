class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)


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

    def test_render_bookings_page(self):
        response = self.client.get(reverse('bookings'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_list.html')


    def test_render_my_bookings_page(self):
        response = self.client.get(reverse('my_bookings'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')   
    
    
    This is a POST view, so use with mockup data.
    def test_render_make_booking(self):
        response = self.client.get(reverse('make_booking'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)


    def test_render_edit_bookings(self):
        response = self.client.get(reverse('edit_booking'))
        # print(response.content)
        self.assertEqual(response.status_code, 200)

    

    self.assertIn(b"Jimmy", response.content)
        self.assertIn(b"2024-07-04", response.content)
        self.assertIn(b"Sheet 1 at 18:00", response.content)
        self.assertIn(b"Required", response.content)
        self.assertIsInstance(response.context['booking_form'], BookingForm)
