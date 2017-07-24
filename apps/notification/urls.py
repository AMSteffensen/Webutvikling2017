from django.conf.urls import url
from . import views

urlpatterns = [

    # Handle Team Request
    url(r'^team/handle-request/$', views.team_handel_req, name='handle-team-req'),

]
