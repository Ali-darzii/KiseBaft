from django import template

register = template.Library()


@register.filter(name='calculate_box_delay')
def calculate_box_delay(value):
    a = value
    return 100 + (value * 50)
