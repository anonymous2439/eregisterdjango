from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.Profile.as_view(), name='accounts-profile'),
    path('profile/<int:user_id>', views.OtherProfile.as_view(), name='accounts-other-profile'),
    path('login/', views.Login.as_view(), name='accounts-login'),
    path('logout/', views.logout, name='accounts-logout'),
    path('manage/', views.ManageAccounts.as_view(), name='accounts-manage'),
    path('dashboard/', views.Dashboard.as_view(), name='accounts-dashboard'),
    path('unauthorized/', views.unauthorized, name='accounts-unauthorized'),
]
