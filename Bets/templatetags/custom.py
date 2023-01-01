from django.template import Library

register = Library()


@register.simple_tag
def set(value):
    return value
