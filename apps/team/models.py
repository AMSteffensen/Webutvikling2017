from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from snippets.unique_slug import unique_slugify


class TeamManager(models.Manager):
    def get_queryset(self):
        return super(TeamManager, self).get_queryset()


class Team(models.Model):
    STATUS_CHOICES = (
        ('shown', 'Offentlig'),
        ('hidden', 'Skjult'),
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, blank=True)
    desc = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='team_author')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    objects = models.Manager()
    everything = TeamManager()


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
    joined = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return "{} is a member of {}".format(self.user_id, self.team_id)

# INSERT INTO TeamUsers
# (team_id, user_id)
# VALUES
# ('1', '1');