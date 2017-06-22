from django.conf.urls import url
from . import views


urlpatterns = [

    # List jobs
    url(r'^$', views.post_list, name='post_list'),
    # Detail jobs
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

    # Create jobs
    url(r'^create/$', views.post_create, name='post_create'),

]