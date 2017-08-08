from django.contrib import admin
from .models import Profile
from .models import WorkHour

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth', 'photo']

class WorkHourAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_date', 'work_project', 'work_category', 'work_duration', 'work_note']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorkHour, WorkHourAdmin)
