from django import forms
from .models import GalleryImage


class GalleryForm(forms.ModelForm):
    """
    This enables users to upload images and
    captions where they will be stored within the
    GalleryImage model.
    """
    class Meta:
        model = GalleryImage
        fields = ('gallery_image', 'caption',)
