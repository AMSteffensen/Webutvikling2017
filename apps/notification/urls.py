from django.conf.urls import url
from . import views_ajax

urlpatterns = [

    # Handle Team Request
    url(r'^team/handle-request/$', views_ajax.team_handle_req, name='handle-team-req'),
    # Handle Team Invites
    url(r'^team/handle-invites/$', views_ajax.team_handel_inv, name='handle-team-inv'),
]
