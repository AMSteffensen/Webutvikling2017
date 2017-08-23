from django.contrib.auth.models import User
from django.db import models


class MessageRelationManager(models.Manager):
    def connections(self, userObj):
        return super(MessageRelationManager, self).get_queryset().filter(models.Q(userA=userObj) | models.Q(userB=userObj))


class MessageRelation(models.Model):
    userA = models.ForeignKey(User, related_name='userA')
    userB = models.ForeignKey(User, related_name='userB')
    read = models.BooleanField(default=False)

    get = MessageRelationManager()

    def __str__(self):
        return '{} <-> {}'.format(self.userA, self.userB)



class MessageManager(models.Manager):
    def by_id(self, msg_id, sort_date=True, msg_count=20):
        if sort_date:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id).order_by('created')[-msg_count:]
        else:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id)[-msg_count:]


class Message(models.Model):

    msg_id = models.ForeignKey(MessageRelation, related_name='msgRel')
    user_from = models.ForeignKey(User, related_name='user_from_msg')
    user_to = models.ForeignKey(User, related_name='user_to_msg')
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    get = MessageManager()