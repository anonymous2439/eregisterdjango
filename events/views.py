from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from accounts.models import User
from events.models import Event, EventType


class Home(View):
    name = 'events/index.html'

    def get(self, request):
        context = {
            'events': Event.objects.all(),
        }
        return render(request, self.name, context)


class AddEvent(View):
    name = 'events/add.html'

    def get(self, request):
        context = {
            'eventTypes': EventType.objects.all(),
        }
        return render(request, self.name, context)

    def post(self, request):
        name = request.POST.get('name', '')
        venue = request.POST.get('venue', '')
        event_type = int(request.POST.get('event-type', '0'))
        organizer = request.user
        print(f'{name} / {venue} / {event_type}')
        event = Event(name=name, venue=venue, event_type=EventType.objects.get(pk=event_type), organizer=organizer).save()
        return HttpResponseRedirect(self.request.path_info)