from django.contrib import admin

from events.models import Event, EventType, Link, EventParticipant

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Link)
admin.site.register(EventParticipant)