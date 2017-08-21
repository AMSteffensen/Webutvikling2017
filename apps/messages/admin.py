from django.contrib import admin
from .models import MessageRelation


class MessageRelationAdmin(admin.ModelAdmin):
    list_display = ('userA', 'userB', 'read')


admin.site.register(MessageRelation, MessageRelationAdmin)