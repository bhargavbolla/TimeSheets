from django.contrib import admin

from UserTimes.models import User123, TimeSheet123, UserProfile


class Timeinline(admin.StackedInline):
    model = TimeSheet123
    extra = 3


class UserAdmin(admin.ModelAdmin):
    inlines = [Timeinline]

admin.site.register(UserProfile)

admin.site.register(User123, UserAdmin)
# Register your models here.
