from . import views
from django.urls import path

urlpatterns = [
    path('', views.NetworkList.as_view(), name='network'),
]