from django.db import models
from django.contrib.auth.models import User

from enum import Enum
from enum import unique

@unique
class NotificationActions(Enum):
    none = 0
    team_req_join = 1
    team_req_acc = 2
    team_req_dec = 3
    team_invite = 4
    team_invite_acc = 5
    team_invite_dec = 6

@unique
class NotificationContexts(Enum):
    none = 0
    team = 1
    project = 2
    user = 3


class NotificationManager(models.Manager):
    def unread(self, user_id):
        return super(NotificationManager, self).get_queryset().filter(user_to=user_id, read=False)
    def read(self, user_id):
        return super(NotificationManager, self).get_queryset().filter(user_to=user_id, read=True)
    def pending_team_req(self, user_id):
        reqObjs = super(NotificationManager, self).get_queryset().filter(
            user_from=user_id,
            context=NotificationContexts.team.name,
            action=NotificationActions.team_req_join.name,
            read=False,
        )
        return [getattr(teamReq, 'foreignPK') for teamReq in reqObjs]

    def pending_team_inv(self, team_id):
        invObjs = super(NotificationManager, self).get_queryset().filter(
            foreignPK=team_id,
            context=NotificationContexts.team.name,
            action=NotificationActions.team_invite.name,
            read=False,
        )
        return [getattr(teamInv, 'user_to') for teamInv in invObjs]


class Notification(models.Model):

    actions = NotificationActions
    contexts = NotificationContexts

    CONTEXT_TYPE = (
        (contexts.none.name, 'none'),
        (contexts.team.name, 'team'),
        (contexts.project.name, 'project'),
        (contexts.user.name, 'user'),
    )

    ACTION_TYPE = (
        (actions.none.name, 'none'),
        (actions.team_req_join.name, 'ønsker å bli med i ditt team'),
        (actions.team_req_acc.name, 'har godtatt ditt team forespørsel'),
        (actions.team_req_dec.name, 'har avslått ditt team forespørsel'),
        (actions.team_invite.name, 'har invitert deg til team'),
        (actions.team_invite_acc.name, 'har godtatt din team invitasjon'),
        (actions.team_invite_dec.name, 'har avslått din team invitasjon'),
    )

    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User, related_name='user_to')
    foreignPK = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    url = models.URLField(blank=True)

    context = models.CharField(max_length=10, choices=CONTEXT_TYPE, default=contexts.none.name)
    action = models.CharField(max_length=25, choices=ACTION_TYPE, default=actions.none.name)

    objects = models.Manager()
    get = NotificationManager()


    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return "{}, {} -> {}".format(self.context, self.user_from, self.user_to)