from django.shortcuts import render
from django.views import generic
from .models import GalleryImage
from .forms import GalleryForm


# Create your views here.
class GalleryImageList(generic.ListView):
    queryset = GalleryImage.objects.all()
    template_name = 'galleryimage_list.html'



def add_image(request):
    if request.method == "POST":
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
        "galleryimage_list.html",
        {"gallery_form": gallery_form
        },
    )



#def AddImage(request):
#    if request.method == "POST":
#        gallery_form = GalleryForm(data=request.POST)
#        if gallery_form.is_valid():
#            gallery_image = gallery_form.save(commit=False)
#            gallery_image.username = request.user
#            gallery_image.save()
#            messages.add_message(
#                request, messages.SUCCESS,
#                'Image submitted and awaiting approval'
#            )

#    gallery_form = GalleryForm()
#    return render(
#        request,
#        "galleryimage_list.html",
#        {"gallery_form": gallery_form
#        },
#    )

