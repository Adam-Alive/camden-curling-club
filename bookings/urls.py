from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
    path('', views.BookingList.as_view(), name='bookings'),    
    path('bookings/my_bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/edit_bookings/<int:booking_id>', views.edit_booking, name='edit_booking'),
   ]