"""обработчик для события создания нового юзера"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(instance,**kwargs):
    """добавляет юзера в группу по его роли"""
    #if created:
    group,created = Group.objects.get_or_create(name=instance.role)
    if not instance.groups.filter(id=group.id).exists():
        instance.groups.clear()
        instance.groups.add(group)
