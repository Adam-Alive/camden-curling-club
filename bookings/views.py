from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


# Create your views here.
#class BookingList(generic.ListView):
#    queryset = Booking.objects.all()
#    template_name = 'booking_list.html'

@login_required
def make_booking(request):
    #gallery_images = GalleryImage.objects.filter(approved=True)
    if request.method == "POST":
        booking_form = BookingForm(request.POST, request.FILES)
        if booking_form.is_valid():
            booking_form.instance.username = request.user
            booking_form.save()
            messages.success(
                request, 'Thank you - your booking is confirmed.'
            )
            return redirect(reverse('make_booking'))

    booking_form = BookingForm()
    template = "bookings/booking_list.html"
    context = {
        "booking_form": booking_form,
        #'gallery_images': gallery_images,
    }

    return render(request, template, context)





