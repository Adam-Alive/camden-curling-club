from django.test import TestCase
from django.urls import reverse
from .forms import GalleryForm

# Create your tests here.

class TestGalleryForm(TestCase):
    """
    Test for the validity of data handled by
    the GalleryForm and Gallery Model.
    """ 
    def test_form_is_valid(self): 
        gallery_form = GalleryForm(
            {'gallery_image': 'image',
             'caption': 'test caption'
        }
        ) 
        self.assertTrue(gallery_form.is_valid())

    def test_form_is_invalid(self): 
        gallery_form = GalleryForm(
            {'gallery_image': 'image',
             'caption': ''
        }
        ) 
        self.assertFalse(gallery_form.is_valid())