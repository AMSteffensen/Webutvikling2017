from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField

from team.models import Team
from team.models import TeamUser


class ContactManager(models.Manager):
    def isFollowing(self, user_id):
        contacts = super(ContactManager, self).get_queryset().filter(user_from=user_id)
        return [getattr(follows, 'user_to') for follows in contacts]
    def followers(self, user_id):
        contacts = super(ContactManager, self).get_queryset().filter(user_to=user_id)
        return [getattr(follower, 'user_from') for follower in contacts]


class Profile(models.Model):
    GENDER_CHOICES = (
        ('mann', 'Mann'),
        ('kvinne', 'Kvinne'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    photo = ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


    objects = models.Manager()
    get = ContactManager()


# Add following field to User dynamically
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
# Add team field to User dynamically
User.add_to_class('member_of_team', models.ManyToManyField(Team, through=TeamUser, related_name='teammember', symmetrical=False))









