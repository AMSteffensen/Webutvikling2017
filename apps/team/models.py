from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from snippets.unique_slug import unique_slugify


class TeamManager(models.Manager):
    def public(self):
        return super(TeamManager, self).get_queryset().filter(status='public')
    def private(self):
        return super(TeamManager, self).get_queryset().filter(status='private')


class TeamUserManager(models.Manager):
    def members(self, team_id):
        teamUserObjs = super(TeamUserManager, self).get_queryset().filter(team_id=team_id)
        return [getattr(member, 'user_id') for member in teamUserObjs]
    def memberOf(self, user_id):
        teamUserObjs = super(TeamUserManager, self).get_queryset().filter(user_id=user_id)
        return [getattr(teamObj, 'team_id') for teamObj in teamUserObjs]

class TeamJoinManager(models.Manager):
    def pending(self, user_id):
        teamJoinObjs = super(TeamJoinManager, self).get_queryset().filter(user_ask=user_id)
        return [getattr(teamReq, 'team_id') for teamReq in teamJoinObjs]


class Team(models.Model):
    STATUS_CHOICES = (
        ('public', 'Offentlig'),
        ('private', 'Skjult'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)
    desc = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='team_author')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    objects = models.Manager()
    get = TeamManager()

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.name


    def save(self, **kwargs):
        slug_str = "{}".format(self.name)
        unique_slugify(self, slug_str)
        super(Team, self).save(**kwargs)


    def get_absolute_url(self):
        return reverse('team:team_detail', args=[self.slug])

# INSERT INTO Team
# (name, desc, author)
# VALUES
# ('Best Team', 'This is the best team', '1');


class TeamUser(models.Model):
    team_id = models.ForeignKey(Team)
    user_id = models.ForeignKey(User)
    joined = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    get = TeamUserManager()

    class Meta:
        ordering = ('-team_id',)

    def __str__(self):
        return "{} is a member of {}".format(self.user_id, self.team_id)


# INSERT INTO TeamUsers
# (team_id, user_id)
# VALUES
# ('1', '1');


class TeamJoin(models.Model):
    user_ask = models.ForeignKey(User)
    team_id = models.ForeignKey(Team)
    asked = models.DateTimeField(auto_now_add=True)
    invited = models.BooleanField()
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-team_id',)

    objects = models.Manager()
    get = TeamJoinManager()
