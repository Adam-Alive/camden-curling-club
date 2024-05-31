from . import views
from django.urls import path

urlpatterns = [
    path('', views.GalleryImageList.as_view(), name='gallery'),
]