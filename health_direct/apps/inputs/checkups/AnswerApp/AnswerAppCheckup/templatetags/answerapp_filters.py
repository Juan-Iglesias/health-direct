from django import template

register = template.Library()

@register.filter(name='index')
def index(value, arg):
    'returns the index of an element in a list'
    return value.index(arg)