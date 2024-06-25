from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.


class TestHomeViews(TestCase):

    def test_render_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html', 'base.html')
