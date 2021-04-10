from django.shortcuts import render
from django.views import View

from accounts.models import User


class Home(View):
    name = 'events/index.html'

    def get(self, request):
        user = User.objects.get(pk=4)
        context = {
            'user': user,
        }
        return render(request, self.name, context)
