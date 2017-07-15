from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login

from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done

from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

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
    url(r'^users/settings/$', views.user_settings, name='user_settings'),
    url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
]
