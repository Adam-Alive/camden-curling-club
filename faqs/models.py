from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Faq(models.Model):
    """
    Stores a single question/answer pair value for faqs.
    """
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
