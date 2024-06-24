from django.shortcuts import render
from django.views import generic
from .models import Faq


class FaqList(generic.ListView):
	"""
	Accesses list of Faqs for use by the
	site administrator and display on the Faqs
	page.
	"""
	queryset = Faq.objects.all()
	template_name = 'faq_list.html'
