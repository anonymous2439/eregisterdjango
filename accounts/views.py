from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from accounts.models import User


class Profile(View):
    name = 'accounts/profile.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
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
            return redirect('events-home')
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


def logout(request):
    auth_logout(request)
    messages.success(request, 'You are now logged out from the system...')
    return redirect('/')
