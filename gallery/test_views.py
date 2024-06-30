from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import GalleryImage
from .forms import GalleryForm

# Create your tests here.


class TestGalleryViews(TestCase):
    """
    Test views from the views.py file.
    """

    def setUp(self):
        """
        Set up test user and booking
        to test CRUD functionality.
        """
        self.user = User.objects.create_user(
            username="Jimmy",
            password="myPassword"
        )

        self.gallery_image = GalleryImage(
            username=self.user,
            gallery_image="image",
            caption="test caption",
            caption_updated_on="2025-01-29",
            approved=True
            )
        self.gallery_image.save()

    def test_render_gallery_page(self):
        self.client.login(username='Jimmy', password='myPassword')
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_render_my_pictures_page(self):
        self.client.login(username='Jimmy', password='myPassword')
        response = self.client.get(reverse('my_pictures'))
        self.assertEqual(response.status_code, 200)
