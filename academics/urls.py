from django.urls import path

from . import views

urlpatterns = [
    path('add-academic-data/', views.addAcademics, name="add-academic-data"),
    path('add-units/', views.addUnits, name="add-units"),
    path('register-units/', views.registerUnits, name="register-units"),
    path('my-units/', views.myUnits, name="my-units"),
    path('attendance/', views.attendance, name="attendance"),
    path('my-attendance/', views.myAttendance, name="my-attendance"),
    path('view-attendance/', views.viewAttendance, name="view-attendance"),
]
