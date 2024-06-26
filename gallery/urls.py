from . import views
from django.urls import path

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('my_pictures/', views.my_pictures, name='my_pictures'),
    path('edit_caption/<galleryimage_id>', views.edit_caption,
         name='edit_caption'),
    path('delete_picture/<galleryimage_id>', views.delete_picture,
         name='delete_picture'),
]
