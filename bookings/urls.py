from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
    path('', views.BookingList.as_view(), name='bookings'),
    path('', views.edit_booking, name='edit_booking'),
   ]