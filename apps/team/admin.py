from django.contrib import admin
from .models import Team
from .models import TeamUser


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'desc', 'author', 'created')
    ordering = ['created',]

class TeamUserAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'user_id', 'joined')
    ordering = ['joined',]

    def get_name(self, obj):
        return obj.team_id.name

class TeamJoinAdmin(admin.ModelAdmin):
    list_display = ('user_ask', 'team_id', 'asked', 'invited', 'accepted')
    ordering = ['team_id',]

admin.site.register(Team, TeamAdmin)
admin.site.register(TeamUser, TeamUserAdmin)