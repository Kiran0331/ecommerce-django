from django import template

register=template.Library()
@register.filter
def multiply(val, arg):
    return float(val) * float(arg)