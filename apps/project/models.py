from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Project(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Mal'),
        ('published','Publisert'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    author = models.ForeignKey(User, related_name='project_post')
    body = models.TextField()
    publish = models.DateTimeField(default=lambda: timezone.localtime(timezone.now()))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        local_pub_date = timezone.localtime(self.publish)
        return reverse('project:project_detail', args=[
            local_pub_date.year,
            local_pub_date.strftime('%m'),
            local_pub_date.strftime('%d'),
            self.slug
        ])
