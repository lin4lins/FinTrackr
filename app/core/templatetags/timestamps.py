from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def get_data_from_timestamp(datetime_obj: datetime):
    formatted_timestamp = datetime_obj.strftime("%H:%M %d.%m.%Y")
    return formatted_timestamp
