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

    url(r'^stats/', views.user_stats, name='user_stats'),
    url(r'^add-hours/', views.user_stats_add_hours, name='stats_add_hours'),
    url(r'^feed/', views.user_feed, name='user_feed'),
]
