from django.shortcuts import render
from django.views import generic
from .models import Network

# Create your views here.


class NetworkList(generic.ListView):
    """
    Accesses list of Network for use by the
    site administrator and display on the Network page.
    """
    queryset = Network.objects.all()
    template_name = 'network_list.html'
