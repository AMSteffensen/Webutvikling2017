from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views
from user.views import dashboard



urlpatterns = [

    # Landing page index
    url(r'^$', views.landing, name='landing'),
]