from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='events-home'),
    path('add/', views.AddEvent.as_view(), name='events-add'),
]
