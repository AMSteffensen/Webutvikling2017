from django.db import models
from django.contrib.auth.models import User


class NotificationManager(models.Manager):
    def unread(self):
        return super(NotificationManager, self).get_queryset().filter(read=False)



class Notification(models.Model):
    CONTEXT_TYPE = (
        ('team', 'team'),
        ('project', 'project'),
        ('user', 'user'),
    )

    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User, related_name='user_to')
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    url = models.URLField(blank=True)

    context = models.CharField(max_length=10, choices=CONTEXT_TYPE)

    objects = models.Manager()
    unread = NotificationManager()


    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return "{}, {} -> {}".format(self.context, self.user_from, self.user_to)

