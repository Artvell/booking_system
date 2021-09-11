from django.db import models

class Hall(models.Model):
    objects = models.Manager()
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name
