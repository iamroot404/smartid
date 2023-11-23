from django.contrib import admin
from .models import AcademicDetails, Units, RegisterUnits, Attendance

# Register your models here.
admin.site.register(AcademicDetails)
admin.site.register(Units)
admin.site.register(RegisterUnits)
admin.site.register(Attendance)