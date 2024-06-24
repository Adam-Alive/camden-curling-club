from django.shortcuts import render, reverse, redirect, get_object_or_404
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
    user_booking = Booking.objects.filter(username=request.user)
    booking_form = BookingForm(request.POST or None)
    if request.method == "POST":
        if booking_form.is_valid():
            booking_form.instance.username = request.user
            booking_form.save()
            messages.success(request,
                             'Thank you - your booking is confirmed.')
    return redirect(reverse('make_booking'))

    template = "bookings/booking_list.html"
    context = {
        "user_booking": user_booking,
        "booking_form": booking_form,
    }
    return render(request, template, context)


@login_required
def my_bookings(request):
    user_booking = Booking.objects.filter(username=request.user)
    booking_form = BookingForm(request.POST or None)
    if request.method == "POST":
        if booking_form.is_valid():
            booking_form.instance.username = request.user
            booking_form.save()
            return redirect(reverse('my_bookings'))

    booking_form = BookingForm()
    template = "bookings/my_bookings.html"
    context = {
        "user_booking": user_booking,
        "booking_form": booking_form,
    }

    return render(request, template, context)


@login_required
def edit_booking(request, booking_id):
    """
    To edit a booking for the current user.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if not booking.username == request.user:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('my_bookings')

    booking_form = BookingForm(request.POST or None, instance=booking)

    if request.method == 'POST':
        if booking_form.is_valid():
            booking_form.instance.username = booking.username
            booking_form.save()
            messages.success(request,
                             'Thank you - your new booking is confirmed.'
                             )
            return redirect(reverse('my_bookings'))

    template = "bookings/edit_bookings.html"
    context = {
        "booking": booking,
        "booking_form": booking_form,
    }
    return render(request, template, context)


@login_required
def delete_booking(request, booking_id):
    """
    To delete a booking for the current user.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if not booking.username == request.user:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('my_bookings')

    booking.delete()
    messages.success(request,
                     'Thank you - your booking has been cancelled.'
                     )
    return redirect(reverse('my_bookings'))
