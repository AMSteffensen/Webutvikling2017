from django.conf.urls import url

from . import views

urlpatterns = [

    # Messages
    url(r'^$', views.messages, name='messages'),

    # New Message
    url(r'^new-message/$', views.new_message, name='new_message'),
]
