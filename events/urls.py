from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='events-home'),
    path('attendance/<str:code>', views.Attendance.as_view(), name='events-attendance'),
]
