from django import template

register = template.Library()


@register.filter(name='sub')
def sub(subtractee, subtractor):
    return subtractee - subtractor


@register.filter(name='mul')
def mul(multiplier, multiple):
    return multiplier * multiple
