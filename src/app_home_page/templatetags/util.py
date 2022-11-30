from django import template

register = template.Library()

@register.filter
def is_dict(value):
    return type(value) is dict

# @register.inclusion_tag(takes_context=True)
# def counter_item_accordion(context):
#     return len(context['data_for_accordion'])