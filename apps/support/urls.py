from django.conf.urls import url
from . import views


urlpatterns = [

    # About
    url(r'^about/$', views.about, name='about'),

    # Contact
    url(r'^contact/$', views.contact, name='contact'),
]
