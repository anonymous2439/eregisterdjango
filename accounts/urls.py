from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.Profile.as_view(), name='accounts-profile'),
    path('login/', views.Login.as_view(), name='accounts-login'),
    path('logout/', views.logout, name='accounts-logout'),
    path('manage/', views.ManageAccounts.as_view(), name='accounts-manage'),
    path('unauthorized/', views.unauthorized, name='accounts-unauthorized'),
]
