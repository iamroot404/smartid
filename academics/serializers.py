from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Units, RegisterUnits, Attendance
from department.serializers import CourseSerializer
from accounts.serializers import UserProfileSerializer

class UnitsSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    course = CourseSerializer(many=False)

    class Meta:
        model = Units
        fields = '__all__'


class RegisterUnitsSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    unit_id = UnitsSerializer(many=False)
    student = UserProfileSerializer(many=False)

    class Meta:
        model = RegisterUnits
        fields = '__all__'


 
class AttendanceSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    unit_id = RegisterUnitsSerializer(many=False)
    
    class Meta:
        model = Attendance
        fields = '__all__'
