from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'priority', 'extent', 'status', 'progress')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['status', 'created']


admin.site.register(Project, ProjectAdmin)
