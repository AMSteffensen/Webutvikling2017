from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from snippets.unique_slug import unique_slugify
from team.models import Team


def get_current_timezone():
    return timezone.localtime(timezone.now())


class ProjectManager(models.Manager):
    def open(self):
        return super(ProjectManager, self).get_queryset().filter(status='open')
    def active(self):
        return super(ProjectManager, self).get_queryset().filter(status='active')
    def finished(self):
        return super(ProjectManager, self).get_queryset().filter(status='finished')
    def closed(self):
        return super(ProjectManager, self).get_queryset().filter(status='closed')


class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Åpen'),
        ('active', 'Aktiv'),
        ('finished', 'Ferdig'),
        ('closed', 'Lukket'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Lav'),
        ('medium', 'Medium'),
        ('high', 'Høy'),
    )

    EXTENT_CHOICES = (
        ('tiny', 'Mini'),
        ('small', 'Liten'),
        ('medium', 'Medium'),
        ('big', 'Stor'),
        ('massive', 'Massiv'),
    )

    # Project
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(User, related_name='project_post')
    body = models.TextField()

    # DateTime
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    # Deal
    deadline = models.DateTimeField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)

    # Info
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    extent = models.CharField(max_length=10, choices=EXTENT_CHOICES, default='medium')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    progress = models.PositiveSmallIntegerField(default=0)

    # External Source
    pr_team = models.ForeignKey(Team, blank=True, null=True)


    objects = models.Manager()
    get = ProjectManager()

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.title


    def save(self, **kwargs):
        slug_str = "{}".format(self.title)
        unique_slugify(self, slug_str)
        super(Project, self).save(**kwargs)


    def get_absolute_url(self):
        local_pub_date = timezone.localtime(self.created)
        return reverse('proj:project_detail', args=[
            local_pub_date.year,
            local_pub_date.strftime('%m'),
            local_pub_date.strftime('%d'),
            self.slug
        ])

    def get_edit_url(self):
        local_pub_date = timezone.localtime(self.created)
        return reverse('proj:project_edit', args=[
            local_pub_date.year,
            local_pub_date.strftime('%m'),
            local_pub_date.strftime('%d'),
            self.slug,
        ])
