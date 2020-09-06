from django import template

register = template.Library()


@register.filter(name='f_range')
def f_range(val=0):
    return range(val)
