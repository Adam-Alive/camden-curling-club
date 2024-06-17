from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
    path('', views.BookingList.as_view(), name='bookings'),    
    path('bookings/my_bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/edit_bookings/<booking_id>', views.edit_booking, name='edit_booking'),
    path('bookings/delete_booking/<booking_id>', views.delete_booking, name='delete_booking'),
   ]