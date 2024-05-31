from django.shortcuts import render
from django.views import generic
from .models import GalleryImage
# from django.http import HttpResponse

# Create your views here.
# def my_faqs(request):
#	return HttpResponse("Hello, curlers!")

class GalleryImageList(generic.ListView):
    queryset = GalleryImage.objects.all()
    template_name = 'galleryimage_list.html'