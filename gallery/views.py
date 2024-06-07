from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import GalleryImage
from .forms import GalleryForm


# Create your views here.
class GalleryImageList(generic.ListView):
    queryset = GalleryImage.objects.all()
    template_name = 'galleryimage_list.html'


def add_image(request):
    if request.method == "POST":
        print('Received a POST request')
        gallery_form = GalleryForm(data=request.POST)
        if gallery_form.is_valid():
            gallery_form.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Image submitted and awaiting approval'
            )

    gallery_form = GalleryForm()


    return render(
        request,
        "gallery/galleryimage_list.html",
        {"gallery": gallery,
        "gallery_form": gallery_form},
    )
