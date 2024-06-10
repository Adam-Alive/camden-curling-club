from . import views
from django.urls import path

urlpatterns = [
    path('', views.GalleryImageList.as_view(), name='gallery'),
    path('galleryimage_list/', views.add_image, name='add_image'),
]