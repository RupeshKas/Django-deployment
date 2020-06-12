from django import template

register = template.Library()


# First method with decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    Cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')


# This is 2nd method to register custom template tag
register.filter('cut', cut)  # 1st is what we call in template, 2nd is function name
