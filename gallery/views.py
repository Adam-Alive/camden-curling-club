from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GalleryImage
from .forms import GalleryForm


## Create your views here.
#class GalleryImageList(generic.ListView):
#    queryset = GalleryImage.objects.all()
#    template_name = 'galleryimage_list.html'

@login_required
def gallery(request):
    gallery_images = GalleryImage.objects.filter(approved=True)
    if request.method == "POST":
        gallery_form = GalleryForm(request.POST, request.FILES)
        if gallery_form.is_valid():
            gallery_form.instance.username = request.user
            gallery_form.save()
            messages.success(
                request, 'Thank you - image submitted and awaiting approval.'
            )
            return redirect(reverse('gallery'))

    gallery_form = GalleryForm()
    template = "gallery/galleryimage_list.html"
    context = {
        "gallery_form": gallery_form,
        'gallery_images': gallery_images,
    }

    return render(request, template, context)


@login_required
def my_pictures(request):
    gallery_images = GalleryImage.objects.filter(approved=True)
    gallery_form = GalleryForm(request.POST, request.FILES)


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
