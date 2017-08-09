from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # admin panel
    url(r'^admin/', admin.site.urls),
    # front page
    #url(r'^$', dashboard),

    # Landing page index
    url(r'^', include('front_page.urls', namespace='front', app_name='front_page')),

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
    url(r'^support/', include('support.urls', namespace='sup', app_name='support')),

    # Notifications
    url(r'^notif/', include('notification.urls', namespace='noti', app_name='notifications')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
