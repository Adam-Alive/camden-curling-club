from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.

def home_page(request):
	#template_name = 'index.html'
    return HttpResponse('This is the home page!')