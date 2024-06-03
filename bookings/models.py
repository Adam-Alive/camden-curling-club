from django.db import models
from django.contrib.auth.models import User

# Create your models here.


SESSION = (
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
    *** TBC Stores a single booking entry.
    """
    username = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name='TBC+'
    )
    date = models.DateField()
    session = models.CharField(choices=SESSION)
    wheelchair_sheet = models.CharField(choices=WHEELCHAIR_SHEET)


    def __str__(self):
        return f'{self.session} booked by {self.username}'