from django.contrib import admin
from .models import MessageRelation
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('msg_id', 'user_from', 'user_to', 'created', 'message')


class MessageRelationAdmin(admin.ModelAdmin):
    list_display = ('userA', 'userB', 'read')


admin.site.register(Message, MessageAdmin)
admin.site.register(MessageRelation, MessageRelationAdmin)
