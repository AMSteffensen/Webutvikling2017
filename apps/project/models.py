from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from snippets.unique_slug import unique_slugify


def get_current_timezone():
    return timezone.localtime(timezone.now())


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Project(models.Model):
    STATUS_CHOICES = (
        ('published', 'Publisert'),
        ('draft', 'Mal'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    author = models.ForeignKey(User, related_name='project_post')
    body = models.TextField()
    publish = models.DateTimeField(default=get_current_timezone)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title


    def save(self, **kwargs):
        slug_str = "{}".format(self.title)
        unique_slugify(self, slug_str)
        super(Project, self).save(**kwargs)


    def get_absolute_url(self):
        local_pub_date = timezone.localtime(self.publish)
        return reverse('proj:project_detail', args=[
            local_pub_date.year,
            local_pub_date.strftime('%m'),
            local_pub_date.strftime('%d'),
            self.slug
        ])
