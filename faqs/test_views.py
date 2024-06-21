from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Faq

# Create your tests here.


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 0)


class TestFaqsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",            
        )
        self.faq = Faq(question="A Question",
                        answer="An Answer"
                    )
        self.faq.save()

    def test_render_faq_list(self):
        response = self.client.get(reverse('faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"A Question", response.content)
        self.assertIn(b"An Answer", response.content)

