"""файл с тегом time_range для шаблона """
from django import template
import datetime
register = template.Library()

@register.filter(name="time_range")
def time_range(start:datetime.datetime, end:datetime.datetime):
    diff = end-start
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    return hours