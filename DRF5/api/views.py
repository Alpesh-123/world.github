from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework.response import Response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            roll = serializer.validated_data['roll']
            city = serializer.validated_data['name']
            
            return Response({'name':name, 'roll':roll, 'city':city})
            
            
        