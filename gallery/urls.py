from . import views
from django.urls import path

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('my_pictures/', views.my_pictures, name='my_pictures'),
]