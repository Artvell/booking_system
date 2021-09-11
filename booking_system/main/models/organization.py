from django.db import models


class Organization(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=40,verbose_name="Название")
    email = models.EmailField(verbose_name="E-mail", max_length=254, default="mail@mail.com")
    phone = models.CharField(verbose_name="Phone number",max_length=15, default="")
    info = models.TextField(verbose_name="Info",blank=True, null=True)
    address = models.CharField(verbose_name="Address",max_length=255,blank=True, null=True)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"

    def __str__(self):
        return self.name
