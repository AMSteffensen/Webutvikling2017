from django.db import models
from django.contrib.auth.models import User


class NotificationManager(models.Manager):
    def unread(self, user_id):
        return super(NotificationManager, self).get_queryset().filter(user_to=user_id, read=False)
    def read(self, user_id):
        return super(NotificationManager, self).get_queryset().filter(user_to=user_id, read=True)


class Notification(models.Model):
    CONTEXT_TYPE = (
        ('none', 'none'),
        ('team', 'team'),
        ('project', 'project'),
        ('user', 'user'),
    )

    ACTION_TYPE = (
        ('none', 'none'),
        ('team_req_join', 'ønsker å bli med i ditt team'),
        ('team_req_acc', 'har godtatt ditt team forespørsel'),
        ('team_req_dec', 'har avslått ditt team forespørsel'),
    )

    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User, related_name='user_to')
    foreignPK = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    url = models.URLField(blank=True)

    context = models.CharField(max_length=10, choices=CONTEXT_TYPE, default='none')
    action = models.CharField(max_length=25, choices=ACTION_TYPE, default='none')

    objects = models.Manager()
    get = NotificationManager()


    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return "{}, {} -> {}".format(self.context, self.user_from, self.user_to)

