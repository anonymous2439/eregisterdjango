from django.shortcuts import render
from django.views import View

from accounts.models import User
from events.models import Event


class Home(View):
    name = 'events/index.html'

    def get(self, request):
        context = {
            'events': Event.objects.all(),
        }
        return render(request, self.name, context)
