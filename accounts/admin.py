from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, UserRole

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(UserRole)
