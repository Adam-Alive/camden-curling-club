from . import views
from django.urls import path

urlpatterns = [
    path('', views.make_booking, name='make_booking'),
]