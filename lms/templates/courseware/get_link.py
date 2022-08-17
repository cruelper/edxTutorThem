from atexit import register
from django import template
register = template.Library()

@register.filter
def get_link(path):
    return "https://openedx.ssau.ru" + path[0:-5] + "/course"