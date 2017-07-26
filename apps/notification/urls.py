from django.conf.urls import url
from . import views_ajax

urlpatterns = [

    # Handle Team Request
    url(r'^team/handle-request/$', views_ajax.team_handel_req, name='handle-team-req'),

]
