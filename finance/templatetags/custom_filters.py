# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def calculate_average(marks_list):
    if not marks_list:
        return 0.0

    total_marks = sum(mark.marks_obtained for mark in marks_list)
    return total_marks / len(marks_list)