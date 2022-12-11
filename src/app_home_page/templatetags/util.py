from django import template
from django.contrib.auth.models import Group, User

from django.contrib.auth.models import Permission


register = template.Library()


@register.filter
def is_dict(value):
    return type(value) is dict


@register.filter
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        group = None
    return group in user.groups.all()

@register.filter
def discont(price):
    price = price*20/100
    return price