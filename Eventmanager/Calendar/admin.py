from django.contrib import admin

# Register your models here.
from Calendar.models import Event, EventMember

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
