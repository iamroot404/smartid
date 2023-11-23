from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('my-account/', views.studentProfile, name="my-account"),
    path('view-students/', views.viewStudents, name="view-students"),
    path('add-student/', views.addStudent, name="add-student"),
    # path('staff-account/<str:pk>/', views.staffAccount, name="staff-account"),
    # path('activate-staff/<str:pk>/', views.activateStaff, name="activate-staff"),
    # path('deactivate-staff/<str:pk>/', views.deactivateStaff, name="deactivate-staff"),
    # path('make-admin/<str:pk>/', views.makeAdmin, name="make-admin"),
    # path('remove-adminf/<str:pk>/', views.removeAdmin, name="remove-admin"),
]
