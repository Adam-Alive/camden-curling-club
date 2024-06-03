from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faq(models.Model):
    """
    TBC Stores a single value for faqs.
    """
    question = models.TextField()
    answer = models.TextField()
    #updated_on = models.DateTimeField(auto_now=True)
    #profile_image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return self.question
