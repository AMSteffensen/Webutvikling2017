from django.conf.urls import url
from . import views

urlpatterns = [

    # List teams
    url(r'^list/$', views.team_list, name='team_list'),
    # List my teams
    url(r'^list/mine/$', views.team_mine, name='team_mine'),

    # Request to join a team
    url('^request_to_join/$', views.team_req_join, name='team_req_join'),

    # Detail teams
    url(r'^view/(?P<slug>[-\w]+)/$', views.team_detail, name='team_detail'),

    # Create teams
    url(r'^create/$', views.team_create, name='team_create')
]
