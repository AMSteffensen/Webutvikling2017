from django.conf.urls import url

from . import views

urlpatterns = [

    # Messages
    url(r'^$', views.messages, name='messages'),
]
