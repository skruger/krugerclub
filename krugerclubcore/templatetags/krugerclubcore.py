from datetime import time

from django import template


register = template.Library()


@register.filter
def unsnake(value):
    return value.replace('_', ' ').title()


@register.simple_tag(takes_context=True)
def time_select_options(context, selected_time):
    times = dict()
    for i in range(0, 24*60, 30):
        minute = i % 60
        hour = i // 60
        times[time(hour=hour, minute=minute)] = False

    if selected_time:
        times[selected_time] = True
    return sorted(times.items())
