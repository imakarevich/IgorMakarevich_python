from django import template

register = template.Library()

@register.filter
def is_dict(value):
    return type(value) is dict
