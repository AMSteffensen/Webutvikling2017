from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('context', 'user_from', 'user_to', 'created', 'read', 'url')


admin.site.register(Notification, NotificationAdmin)