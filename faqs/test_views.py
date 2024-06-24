from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Faq

# Create your tests here.

class TestFaqsViews(TestCase):
    """
    Tests for login of site administrator
    and validity of faqs data.
    """

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",            
        )
        self.faq = Faq(question="A Question",
                        answer="An Answer"
                    )
        self.faq.save()

    def test_render_faqs_page(self):
        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faq_list.html', 'base.html')
        self.assertIn(b"A Question", response.content)
        self.assertIn(b"An Answer", response.content)
