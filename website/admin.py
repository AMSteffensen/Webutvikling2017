# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Contractor
from .models import Principal
from .models import UserCredential
from .models import Job

admin.site.register(Contractor)
admin.site.register(Principal)
admin.site.register(UserCredential)
admin.site.register(Job)
