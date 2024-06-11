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

#def image_detail(request):
#    """
#    Display a single image.
#    """
#    gallery_images = GalleryImage.objects.filter(approved=True)
#    image = get_object_or_404()
#    author = image.author


#    return render(
#        request,
#        "gallery/galleryimage_list.html",
#        {"author": author,
#        "caption": caption
#        },
#    )

    #queryset = Post.objects.filter(status=1)
    #post = get_object_or_404(queryset, slug=slug)
    #comments = post.comments.all().order_by("-created_on")
    #comment_count = post.comments.filter(approved=True).count()
