from django.conf.urls import url
from . import views

urlpatterns = [

    # List teams
    url(r'^list/$', views.team_list, name='team_list'),

    # Detail teams
    url(r'^view/(?P<slug>[-\w]+)/$', views.team_detail, name='team_detail'),
]
