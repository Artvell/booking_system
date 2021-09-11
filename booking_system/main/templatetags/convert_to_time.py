"""файл с тегом convert_to_time для шаблона """
from django import template
import datetime
register = template.Library()

@register.filter(name="convert_to_time")
def convert_to_time(hour,date:datetime.datetime):
    if not isinstance(date,datetime.datetime):
        if hour.minute >= 30:
            hour = hour.replace(second=0, microsecond=0, minute=0, hour=hour.hour+1)
        else:
            hour = hour.replace(second=0, microsecond=0, minute=0)
        new_date = datetime.datetime.combine(date,hour)
        #print("!", new_date)
        return new_date
    else:
        new_date = date.replace(hour=hour,minute=0,second=0,microsecond=0)
        #print("#",type(new_date))
        return new_date