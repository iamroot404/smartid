from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.addDepartment, name="add-department"),
    path('view-department/', views.viewDepartment, name="view-department"),
    path('add-course/', views.addCourse, name="add-course"),
    path('view-course/', views.viewCourse, name="view-course"),
]
