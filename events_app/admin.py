from django.contrib import admin

from events_app.models import EventUsers, AboutUser, UserGoals
# Register your models here.
admin.site.register(EventUsers)
admin.site.register(AboutUser)
admin.site.register(UserGoals)