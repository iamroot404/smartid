from django.urls import path
from .views import AttendanceAPIView


urlpatterns = [ 
    path('api/attendance/', AttendanceAPIView.as_view(), name='attendance-api'), 
]
