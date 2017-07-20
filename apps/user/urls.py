from django.conf.urls import url
from . import views


urlpatterns = [

    # dashboard
    url(r'^$', views.dashboard, name='dashboard'),

    # profile
    url(r'^edit/$', views.edit, name='edit'),

    # user profiles
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^users/follow/$', views.user_follow, name='user_follow'),
    url(r'^users/relations', views.user_relations, name='user_relation'),
    url(r'^users/settings/$', views.user_settings, name='user_settings'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
]
