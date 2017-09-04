from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views
from user.views import dashboard



urlpatterns = [

    # Landing page index
    url(r'^$', views.landing, name='landing'),


    #Maps
    url(r'^maps/$', TemplateView.as_view(template_name='maps.html'), name='maps'),

    #Upgrade
    url(r'^upgrade/$', TemplateView.as_view(template_name='upgrade.html'), name='upgrade'),
]
