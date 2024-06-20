from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Faq

# Create your tests here.
class FaqList(generic.ListView):   
	queryset = Faq.objects.all()
	template_name = 'faq_list.html'
