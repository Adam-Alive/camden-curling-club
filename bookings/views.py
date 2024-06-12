from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


# Create your views here.
class BookingList(generic.ListView):
    """
    Creates a list of bookings submitted.
    """
    queryset = Booking.objects.all()
    template_name = 'booking_list.html'


@login_required
def make_booking(request):
    """
    Displays booking form and posts booking requests.
    """   
    user_booking = Booking.objects.all()
    if request.method == "POST":        
        booking_form = BookingForm(data=request.POST)      
        if booking_form.is_valid():
            booking_form.save()
            messages.success(
            request, 'Thank you - your booking is confirmed.'
            )
            return HttpResponseRedirect(reverse('make_booking'))

    # user_booking = Booking.objects.all()
    booking_form = BookingForm()
    template = "bookings/booking_list.html"
    context = {
        "user_booking": user_booking,
        "booking_form": booking_form,
    }
    return render(request, template, context)



