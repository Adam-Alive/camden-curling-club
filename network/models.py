from django.db import models
from django.contrib.auth.models import User

# Create your models here.


WHEELCHAIR_ACCESS = (
    ('Yes', 'Yes'),
    ('No', 'No')
)


class Network(models.Model):
    """
    Allows administrator to upload information about
    other curling clubs in England.
    """
    club_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    wheelchair_access = models.CharField(choices=WHEELCHAIR_ACCESS, max_length=150)  # noqa

    def __str__(self):
        return self.club_name
