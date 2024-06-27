from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GalleryImage
from .forms import GalleryForm


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
    user_pictures = GalleryImage.objects.filter(username=request.user,
                                                approved=True)
    if request.method == "POST":
        return redirect(reverse('my_pictures'))

    gallery_form = GalleryForm()
    template = "gallery/my_pictures.html"
    context = {
        "user_pictures": user_pictures,
    }

    return render(request, template, context)


@login_required
def edit_caption(request, galleryimage_id):
    """
    To edit a picture caption for the current user.
    """
    caption = get_object_or_404(GalleryImage, id=galleryimage_id,
                                approved=True)
    if not caption.username == request.user:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('my_pictures')
    gallery_form = GalleryForm(request.POST or None, instance=caption)

    if request.method == 'POST':
        if gallery_form.is_valid():
            gallery_form.instance.username = caption.username
            gallery_form.instance.approved = False
            gallery_form.save()
            messages.success(
                request, 'Thank you - caption changed and awaiting approval.'
            )
            return redirect(reverse('my_pictures'))

    template = "gallery/edit_caption.html"
    context = {
        "caption": caption,
        "gallery_form": gallery_form,
    }
    return render(request, template, context)


@login_required
def delete_picture(request, galleryimage_id):
    """
    To delete a picture and caption for the current user.
    """
    picture = get_object_or_404(GalleryImage, id=galleryimage_id,
                                approved=True)
    if not picture.username == request.user:
        messages.error(request, "Access denied - invalid credentials")
        return redirect('my_pictures')

    if picture.username == request.user:
        picture.delete()
        messages.success(request, 'Thank you - your picture has been deleted.'
                         )
        return redirect(reverse('my_pictures'))
