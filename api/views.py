from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


from academics.models import RegisterUnits, Attendance
from academics.serializers import AttendanceSerializer

# Create your views here.

class AttendanceAPIView(APIView):
    def post(self, request, format=None):
        registration_number = request.data.get('reg')
        unit_code = request.data.get('code')

        try:
            units = RegisterUnits.objects.get(unit_id__unit_code=unit_code, student__registration_number=registration_number)

            if units:
                att = Attendance.objects.create(unit_id=units)
                att.save()
                serializer = AttendanceSerializer(att)
                return Response({'message': 'Attendance was added successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Unit not found'}, status=status.HTTP_404_NOT_FOUND)
        except RegisterUnits.DoesNotExist:
            return Response({'error': 'Unit or student not found'}, status=status.HTTP_404_NOT_FOUND)