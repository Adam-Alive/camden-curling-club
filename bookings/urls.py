from . import views
from django.urls import path

urlpatterns = [
    path('make-booking/', views.make_booking, name='make_booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('edit_bookings/<booking_id>', views.edit_booking, name='edit_booking'),  # noqa
    path('delete_booking/<booking_id>', views.delete_booking, name='delete_booking'),  # noqa
   ]
