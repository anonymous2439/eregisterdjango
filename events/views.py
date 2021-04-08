from django.shortcuts import render
from django.views import View


class Home(View):
    name = 'events/index.html'

    def get(self, request):
        return render(request, self.name)
