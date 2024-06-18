from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GalleryImage
from .forms import GalleryForm, CaptionForm


## Create your views here.
#class GalleryImageList(generic.ListView):
#    queryset = GalleryImage.objects.all()
#    template_name = 'galleryimage_list.html'

@login_required
def gallery(request):
    """
    Allows user to submit an image to be approved by the
    site administrator. After approval, the image and caption
    are displayed on the Gallery page.
    """
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
    """
    Displays the current user's uploaded pictures.
    """
    user_pictures = GalleryImage.objects.filter(username=request.user, approved=True)  
    if request.method == "POST":                 
        return redirect(reverse('my_pictures'))

    gallery_form = GalleryForm()
    template = "gallery/my_pictures.html"
    context = {
        "user_pictures": user_pictures,       
    }

    return render(request, template, context)


@login_required
def edit_caption(request, gallery_image_id):
    """
    To edit a picture caption for the current user.
    """
    caption = get_object_or_404(GalleryImage, id=gallery_image_id)
    if not caption.username == request.user:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('my_pictures')

    caption_form = CaptionForm(request.POST or None, instance=caption)

    if request.method == 'POST':    
        if caption_form.is_valid():
            caption_form.instance.username = request.user
            caption_form.save()
            messages.success(
                request, 'Thank you - caption changed and awaiting approval.'
            )
            return redirect(reverse('my_pictures'))

    template = "gallery/edit_caption.html"
    context = {
        "caption": caption,
        "caption_form": caption_form,
    }
    return render(request, template, context)




# @login_required
# def edit_booking(request, booking_id):
#     """
#     To edit a booking for the current user.
#     """
#     booking = get_object_or_404(Booking, id=booking_id)
#     if not booking.username == request.user:
#         messages.error(request, "Access denied - invalid credentials")
#         return redirect('my_bookings')

#     booking_form = BookingForm(request.POST or None, instance=booking)

#     if request.method == 'POST':
#         if booking_form.is_valid():
#             booking_form.instance.username = booking.username
#             booking_form.save()          
#             messages.success(request,
#                 'Thank you - your new booking is confirmed.'
#             )
#             return redirect(reverse('my_bookings'))

#     template = "bookings/edit_bookings.html"
#     context = {
#         "booking": booking, 
#         "booking_form": booking_form,
#     }
#     return render(request, template, context)