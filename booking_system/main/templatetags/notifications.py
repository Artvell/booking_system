"""файл с тегом notifications для шаблона """
from django import template
from django.db.models import Q
from main.models import Attachment
from datetime import datetime
register = template.Library()

@register.filter(name="notifications")
def notifications(user):
    """шаблонный тег. Возвращает уведомления для юзера"""
    #attachments = Attachment.objects.filter(booking__manager=user)
    attachments = Attachment.objects.filter(Q(booking__manager=user)&Q(booking__notification_date__lte=datetime.now().date()))
    return attachments
