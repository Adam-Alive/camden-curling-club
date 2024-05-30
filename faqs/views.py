from django.shortcuts import render
from django.views import generic
from .models import Faq
#from django.http import HttpResponse

# Create your views here.
#def my_faqs(request):
#	return HttpResponse("Hello, curlers!")

class FaqList(generic.ListView):
    model = Faq

