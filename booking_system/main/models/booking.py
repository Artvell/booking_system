from datetime import datetime
from django.db import models
from main.models import Manager, Organization
from authentification.models import User


class Booking(models.Model):
    choices = [
        ("Tentative", "Tentative"),
        ("Confirmed", "Confirmed"),
        ("Canceled", "Canceled"),
        ("Closed", "Closed")
    ]
    objects = models.Manager()
    start = models.DateTimeField(default=datetime.now())
    end = models.DateTimeField(default=datetime.now())
    client = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name="Client")
    status = models.CharField("Status",default=0,choices=choices, max_length=11)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Organization",default=1)
    manager = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name="Manager")
    comment = models.TextField("Comment", null=True, blank=True)
    attachment = models.FileField("Attachment", null=True, blank=True)
    notification_date = models.DateField("Notification at:",null=True, blank=True)
    total = models.FloatField(default=0)
    def __str__(self):
        return str(self.id)
