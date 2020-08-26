from django import template

register = template.Library()


@register.filter(name='f_range')
def f_range(val=0):
    return range(val)


@register.filter(name='sub')
def sub(subtractor, subtractee):
    return subtractee - subtractor
