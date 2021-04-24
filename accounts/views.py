from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
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


class Login(View):
    name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.name)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome {user.email}')
            if request.POST.get('next'):
                return redirect(request.POST.get('next'))
            return redirect('/events/')
        else:
            messages.error(request, 'Invalid Username/Password')
        return render(request, self.name)


class ManageAccounts(View):
    name = 'accounts/manage.html'

    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, self.name, context)
