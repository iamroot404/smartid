from django.db import models
from accounts .models import UserProfile
from department .models import Course
import uuid
 

# Create your models here.
class AcademicDetails(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # def __str__(self):
    #     return self.student
    class Meta:
        ordering = ['created']


class Units(models.Model):
    unit_name = models.CharField(max_length=200)
    unit_code = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.unit_name
    
    class Meta:
        ordering = ['created']


class RegisterUnits(models.Model):
    unit_id = models.ForeignKey(Units, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # def __str__(self):
    #     return self.unit_id
    
    class Meta:
        ordering = ['created']


class Attendance(models.Model):
    # student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    unit_id = models.ForeignKey(RegisterUnits, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']
