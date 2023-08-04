from django.shortcuts import render
from .serializers import StudentSerializer,CourseSerializer
from .models import Student,Course
from rest_framework import viewsets
from rest_framework.response import Response

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get['name']
            roll = request.data.get['roll']
            city = request.data.get['city']
            country = request.data.get['country']
            
            return Response({'name':name, 'roll':roll, 'city':city, 'country':country})
    
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

