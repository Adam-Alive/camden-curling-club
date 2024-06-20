from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class GalleryImage(models.Model):
    """
    Stores an image and caption entry uploaded
    by the current user.
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    gallery_image = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=100, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)
    caption_updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-caption_updated_on']

    def __str__(self):
        return f'{self.caption} | added by {self.username}'
