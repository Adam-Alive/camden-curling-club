from django.shortcuts import render
from django.views import generic
from .models import GalleryImage

# Create your views here.
class GalleryImageList(generic.ListView):
    queryset = GalleryImage.objects.all()
    template_name = 'galleryimage_list.html'