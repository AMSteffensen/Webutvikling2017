from django.conf.urls import url
from . import views


urlpatterns = [

    # List projects
    url(r'^$', views.project_list, name='project_list'),
    # List my projects
    url(r'^my_posts$', views.project_mine, name='project_mine'),

    # Detail projects
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<project>[-\w]+)/$', views.project_detail, name='project_detail'),

    # Create projects
    url(r'^create/$', views.project_create, name='project_create'),
]
