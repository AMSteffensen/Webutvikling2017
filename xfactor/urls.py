"""xfactor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

from user.views import dashboard


urlpatterns = [
    # admin panel
    url(r'^admin/', admin.site.urls),
    # front page
    url(r'^$', dashboard),

    # About
    url(r'^about/', TemplateView.as_view(template_name='static_pages/about.html'),
        name='about'),
    # Contact us
    url(r'^contact/', TemplateView.as_view(template_name='static_pages/contact.html'),
        name='contact'),
    # Landing page index
    url(r'^landing/', TemplateView.as_view(template_name='static_pages/index.html'),
        name='home'),

    # user authentication app
    url(r'^uauth/', include('user_auth.urls', namespace='uauth', app_name='user_auth')),
    #url(r'^uauth/', include('social_django.urls', namespace='social')),  # <--

    # user app
    url(r'^user/', include('user.urls', namespace='user', app_name='user')),

    # team app
    url(r'^team/', include('team.urls', namespace='team', app_name='team')),

    # project app
    url(r'^project/', include('project.urls', namespace='proj', app_name='project')),

    # contract app
    #url(r'^contract/', include('contract.urls', namespace='ctrt', app_name='contract')),

    # support app
    #url(r'^support/', include('support.urls', namespace='sup', app_name='support')),

    # Notifications
    url(r'^notif/', include('notification.urls', namespace='noti', app_name='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
