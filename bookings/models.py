from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SHEET_TIMES = (
    ('Sheet 1 at 18.00 - 19.30', 'Sheet 1 at 18.00 - 19.30'),
    ('Sheet 2 at 18.00 - 19.30', 'Sheet 2 at 18.00 - 19.30'),
    ('Sheet 3 at 18.00 - 19.30', 'Sheet 3 at 18.00 - 19.30'),
    ('Sheet 1 at 20.00 - 21.30', 'Sheet 1 at 20.00 - 21.30'),
    ('Sheet 2 at 20.00 - 21.30', 'Sheet 2 at 20.00 - 21.30'),
    ('Sheet 3 at 20.00 - 21.30', 'Sheet 3 at 20.00 - 21.30'),
)


WHEELCHAIR_SHEET = (
    ('Not Required', 'Not Required'),
    ('Required', 'Required')
)


class Booking(models.Model):
    """
    *** Stores a single booking entry by a user to
    enable booking, booking amendment and cancellation.
    """
    username = models.ForeignKey(
        User, on_delete=models.CASCADE
        )
    date = models.DateField()
    sheet_time = models.CharField(choices=SHEET_TIMES, max_length=150)
    wheelchair_sheet = models.CharField(
        choices=WHEELCHAIR_SHEET, max_length=150
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.sheet_time} booked by {self.username}'
