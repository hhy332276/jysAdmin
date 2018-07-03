from django.utils.safestring import mark_safe
from django import template
register = template.Library()
import time
@register.filter(name='time_cover')
def time_format(t):
    t1 = time.localtime(t)
    t2 = time.strftime('%Y-%m-%d %H:%M:%S', t1)
    return t2