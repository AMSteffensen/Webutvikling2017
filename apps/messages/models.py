from django.db import models
from django.contrib.auth.models import User



class MessageRelation(models.Model):
    userA = models.ForeignKey(User, related_name='userA')
    userB = models.ForeignKey(User, related_name='userB')
    read = models.BooleanField(default=False)

    def __str__(self):
        return '{} <-> {}'.format(self.userA, self.userB)



class MessageManager(models.Manager):
    def get_by_id(self, msg_id, sort_date=True):
        if sort_date:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id).order_by('created')[-20:]
        else:
            return super(MessageManager, self).get_queryset().filter(msg_id=msg_id)[-20:]


class Message(models.Model):

    msg_id = models.ForeignKey(MessageRelation, related_name='msgRel')
    user_from = models.ForeignKey(User, related_name='user_from_msg')
    user_to = models.ForeignKey(User, related_name='user_to_msg')
    created = models.DateTimeField(auto_now_add=True)
    message = models.TextField()