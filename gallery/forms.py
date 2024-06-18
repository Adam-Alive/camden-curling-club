from django import forms
from .models import GalleryImage

class GalleryForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('gallery_image', 'caption',)


class CaptionForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ('caption',)