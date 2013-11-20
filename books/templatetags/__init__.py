from django import template

register = template.Library()
register.filter('lower',lower)



def lower(value):#only one argument.
    "Convert a string into all lowercase"
    return value.lower()
