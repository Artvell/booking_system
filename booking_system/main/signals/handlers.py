"""обработчик для события создания нового юзера"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from main.models import Attachment, Booking

@receiver(post_save, sender=Booking)
def save_profile(instance,**kwargs):
    attachment,is_created = Attachment.objects.get_or_create(booking=instance)
