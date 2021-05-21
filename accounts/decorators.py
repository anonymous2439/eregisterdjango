from django.http import HttpResponse
from django.shortcuts import redirect


def authenticate_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.role.pk != 1:
            return redirect('accounts-unauthorized')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
