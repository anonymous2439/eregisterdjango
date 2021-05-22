from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.utils import timezone

from accounts.decorators import authenticate_user
from accounts.models import User
from events.models import Event, EventType, EventParticipant


class Home(View):
    name = 'events/index.html'

    @method_decorator(login_required)
    def get(self, request):
        context = {
            'events': Event.objects.all(),
            'eventTypes': EventType.objects.all(),
        }
        return render(request, self.name, context)

    def post(self, request):
        name = request.POST.get('name', '')
        venue = request.POST.get('venue', '')
        event_type = int(request.POST.get('event-type', '0'))
        start_date = request.POST.get('start-date')
        end_date= request.POST.get('end-date')
        organizer = request.user
        print(f'{name} / {venue} / {event_type}')
        event = Event(name=name, venue=venue, event_type=EventType.objects.get(pk=event_type), organizer=organizer, start_date=start_date, end_date=end_date).save()
        return HttpResponseRedirect(self.request.path_info)


class Attendance(View):
    name = 'events/attendance.html'

    @method_decorator(login_required)
    @method_decorator(authenticate_user)
    def get(self, request, code):
        participant = User.objects.get(qr_id=code)
        events = Event.objects.filter(start_date__lt=timezone.now(), end_date__gt=timezone.now(), organizer=request.user)
        for event in events:
            if len(EventParticipant.objects.filter(event=event, user=participant)) == 0:
                EventParticipant(event=event, user=participant).save()
                messages.success(request, 'You joined the event!')
            else:
                messages.warning(request, 'This user has already participated this event!')
        context = {
            'events': events,
            'participant': participant,
        }
        return render(request, self.name, context)

    def post(self, request):
        if request.is_ajax():
            event_id = request.POST.get('event-id')
            user_id = request.POST.get('user-id')
            print(f'{event_id} - {user_id}')
        return redirect('events-home')