from django.db import models
from main.models import Booking

class Attachment(models.Model):
    objects = models.Manager()
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE, related_name="linked_booking")
    def __str__(self):
        return str(self.id)