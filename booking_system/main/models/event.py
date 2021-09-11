from django.db import models
from main.models import Booking, Hall

class Event(models.Model):
    objects = models.Manager()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE,related_name="event")
    hall = models.ForeignKey(Hall,on_delete=models.PROTECT,verbose_name="Hall")
    date = models.DateField("Date")
    start = models.TimeField("Event starts")
    end = models.TimeField("Event ends")
    type_of_seating = models.CharField("Seating",max_length=50,default="")
    event_type = models.CharField("Type",max_length=20)
    attendance = models.IntegerField("Attedance")
    rent = models.FloatField("Rent")
    food = models.FloatField("Food per person")
    beverage = models.FloatField("Beverage per person")
    total = models.FloatField("Total")
    attachment = models.FileField("Attachment", null=True, blank=True)

    def __str__(self):
        return str(self.id)
