from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Network

# Create your tests here.


class TestNetworkViews(TestCase):
    """
    Tests for login of site administrator
    and validity of Network data.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
        )
        self.network = Network(
                        club_name="X Curling Club",
                        location="Anytown",
                        website="curling.website.com",
                        email="club@curling.com",
                        wheelchair_access="Yes"
                        )
        self.network.save()

    def test_render_network_page(self):
        response = self.client.get(reverse('network'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'network/network_list.html', 'base.html')
        self.assertIn(b"X Curling Club", response.content)
        self.assertIn(b"Anytown", response.content)
        self.assertIn(b"curling.website.com", response.content)
        self.assertIn(b"club@curling.com", response.content)
        self.assertIn(b"Yes", response.content)
