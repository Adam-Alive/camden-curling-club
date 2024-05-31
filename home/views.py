from django.shortcuts import render
from django.views import generic
#from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'home/index.html',)