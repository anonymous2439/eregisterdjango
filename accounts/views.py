import hashlib
from io import BytesIO

import qrcode
from PIL import Image, ImageDraw
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from accounts.models import User, UserRole
from events.models import Link


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
        user_roles = UserRole.objects.all()
        context = {
            'users': users,
            'user_roles': user_roles,
        }
        return render(request, self.name, context)

    def post(self, request):
        if request.is_ajax():
            # deleting user
            if request.POST.get('delete') == '1':
                print(request.POST.get('user_id'))
                user = User.objects.get(pk=int(request.POST.get('user_id')))
                user.delete()
                messages.success(request, 'A user has been successfully deleted!')
                return JsonResponse({'success': 1})
            return JsonResponse({'success': 0})
        else:
            home_url = Link.objects.get(name='home_url')
            user = User(
                first_name=request.POST.get('fname'),
                middle_name=request.POST.get('mname'),
                last_name=request.POST.get('lname'),
                email=request.POST.get('email'),
                contact_no=request.POST.get('contact-no'),
                role=UserRole.objects.get(pk=int(request.POST.get('role'))),
            )
            user.set_password('password')
            qrcode_img = qrcode.make(f'{home_url.url}attendance/{hashlib.md5(str(request.POST.get("email")).encode("utf-8")).hexdigest()}')
            user.qr_id = hashlib.md5(str(request.POST.get("email")).encode("utf-8")).hexdigest()
            canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            file_name = f'{hashlib.md5(str(request.POST.get("email")).encode("utf-8")).hexdigest()}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            user.qr_code.save(file_name, File(buffer), save=False)
            canvas.close()
            user.save()
            return redirect('accounts-manage')


def logout(request):
    auth_logout(request)
    messages.success(request, 'You are now logged out from the system...')
    return redirect('/')
