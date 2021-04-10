from django.shortcuts import render
from django.views import View

from accounts.models import User


class Profile(View):
    name = 'accounts/profile.html'

    def get(self, request):
        user = User.objects.get(pk=1)
        context = {
            'user': user,
        }
        return render(request, self.name, context)
