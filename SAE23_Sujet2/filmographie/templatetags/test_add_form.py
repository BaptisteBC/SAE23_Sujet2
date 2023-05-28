from django import template

register = template.Library()

@register.filter        #dit a la suite de se comporter comme un filtre pour le template 
def add_form(value):
    return value.__class__.__name__