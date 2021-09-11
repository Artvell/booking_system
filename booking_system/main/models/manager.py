from django.db import models
from main.models import Organization

class Manager(models.Model):
    objects = models.Manager()
    fullname = models.CharField("Full name", max_length=50)
    email = models.EmailField(verbose_name="E-mail", max_length=254)
    phone = models.CharField(verbose_name="Phone number",max_length=15)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)

    def __str__(self):
        return self.email
