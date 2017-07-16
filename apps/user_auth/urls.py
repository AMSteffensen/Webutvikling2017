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

    # registration
    url(r'^register/$', views.user_register, name='register'),

    # login / logout urls
    url(r'^login/$',
        login,
        {'template_name': 'user_auth/login/login.html'},
        name='login'),

    url(r'^logout/$',
        logout,
        {'template_name': 'user_auth/login/logout.html'},
        name='logout'),

    url(r'^logout-then-login/$',
        logout_then_login,
        name='logout_then_login'),

    # change password urls
    url(r'^password-change/$',
        password_change,
        {'template_name': 'user_auth/password_util/password_change_form.html',
         'post_change_redirect': 'uauth:password_change_done'},
        name='password_change'),

    url(r'^password-change/done/$',
        password_change_done,
        {'template_name': 'user_auth/password_util/password_change_done.html'},
        name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$',
        password_reset,
        {'template_name': 'user_auth/password_util/password_reset_form.html',
         'email_template_name': 'user_auth/password_util/password_reset_email.html',
         'post_reset_redirect': 'uauth:password_reset_done'},
        name='password_reset'),

    url(r'^password-reset/done/$',
        password_reset_done,
        {'template_name': 'user_auth/password_util/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'user_auth/password_util/password_reset_confirm.html',
        'post_reset_redirect': 'uauth:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        password_reset_complete,
        {'template_name': 'user_auth/password_util/password_reset_complete.html'},
        name='password_reset_complete'),
]
