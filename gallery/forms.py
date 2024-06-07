from .models import GalleryImage
from django import forms

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('gallery_image', 'caption',)