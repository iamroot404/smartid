from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Department, Course

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CourseSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    department = DepartmentSerializer(many=False)
   
    class Meta:
        model = Course
        fields = '__all__'