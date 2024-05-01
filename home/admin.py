from django.contrib import admin

from home.models import Room, Talk, Schedule


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Talk)
class TalkAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass
