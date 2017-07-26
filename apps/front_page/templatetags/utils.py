from django import template

from notification.models import Notification
from team.models import Team

from snippets.hasher import encode_value



register = template.Library()

@register.assignment_tag
def my_notifications(request):
    return Notification.get.unread(request.user)

@register.simple_tag
def get_team_name(pk):
    return Team.objects.get(pk=int(pk)).name

@register.simple_tag
def get_team_url(pk):
    return Team.objects.get(pk=int(pk)).get_absolute_url()

@register.simple_tag
def scramble(value):
    return encode_value(value)