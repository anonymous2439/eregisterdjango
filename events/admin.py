from django.contrib import admin

from events.models import Event, EventType, Link

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Link)