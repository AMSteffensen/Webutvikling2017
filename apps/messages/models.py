from django.contrib.auth.models import User
from django.db import models

## MESSAGE RELATIONS
class MessageRelationManager(models.Manager):
    def connections(self, userObj):
        return super(MessageRelationManager, self).get_queryset().filter(models.Q(userA=userObj) | models.Q(userB=userObj))
    def unread(self, user_id):
        return super(MessageRelationManager, self).get_queryset().filter(read=False)


class MessageRelation(models.Model):
    userA = models.ForeignKey(User, related_name='userA')
    userB = models.ForeignKey(User, related_name='userB')
    read = models.BooleanField(default=False)

    objects = models.Manager()
    get = MessageRelationManager()

    def __str__(self):
        return '{} <-> {}'.format(self.userA, self.userB)
## /MESSAGE RELATIONS

## MESSAGES
class MessageManager(models.Manager):
    def by_id(self, msg_id, sort_date=True, msg_count=20):
        if sort_date:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id).order_by('created')[-msg_count:]
        else:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id)[-msg_count:]


class Message(models.Model):
    msg_id = models.ForeignKey(MessageRelation, related_name='msg_id')
    user_from = models.ForeignKey(User, related_name='msg_user_from')
    user_to = models.ForeignKey(User, related_name='msg_user_to')
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    objects = models.Manager()
    get = MessageManager()

    class Meta:
        ordering = ('created',)
## /MESSAGES