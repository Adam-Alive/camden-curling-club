from django.shortcuts import render
from django.views import generic
from .models import Faq


class FaqList(generic.ListView):   
	queryset = Faq.objects.all()
	template_name = 'faq_list.html'
