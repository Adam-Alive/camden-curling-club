from django.shortcuts import render
from django.views import generic
from .models import Network

# Create your views here.

class NetworkList(generic.ListView):
    queryset = Network.objects.all()
    template_name = 'network_list.html'
