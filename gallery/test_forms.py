from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import GalleryForm

# Create your tests here.


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)


class TestCommentForm(TestCase): 
 
    def test_form_is_valid(self): 
        gallery_form = GalleryForm(
            {'gallery_image': 'image',
             'caption': 'test caption'
        }
        ) 
        self.assertTrue(gallery_form.is_valid())