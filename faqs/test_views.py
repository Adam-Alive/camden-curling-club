from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Faq

# Create your tests here.

# class TestBookingsViews(TestCase):

# 	def setUp(self):
# 		self.user = User.objects.create_superuser(
#             username="myUsername",
#             password="myPassword"           
#         )
# 		self.faq = faq(question = "How many?",
#     				answer = "Ten"
# 					)
# 		self.faq.save()


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 0)

