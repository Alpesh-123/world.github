from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action

class PercentageModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(detail=False, methods=['post'])
    def calculate_percentage(self, request):
        #student = self.get_object()
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            maths_marks = serializer.validated_data['maths_marks']
            physics_marks = serializer.validated_data['physics_marks']
            chemistry_marks = serializer.validated_data['chemistry_marks']
            
            total_marks = maths_marks + physics_marks + chemistry_marks
        
            print(total_marks)
            percentage = (total_marks / 300) * 100
        
            print(percentage)
                        
            #student.save()
            return Response({'percentage': percentage})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
