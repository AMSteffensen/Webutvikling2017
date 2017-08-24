from django.conf.urls import url

from . import views
from . import views_ajax

urlpatterns = [

    # Messages
    url(r'^$', views.messages, name='messages'),

    # New Message
    url(r'^new-message/$', views.new_message, name='new_message'),

    # Send Message
    url(r'^send-message/$', views_ajax.send_pm, name='send_pm'),
]
