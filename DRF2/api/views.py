from rest_framework import viewsets 
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import action


class CalculatePercentageViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    @action(methods=["GET"], detail=False)
    def calculate_percentage(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
         total_marks = request.data.get('total_marks')
         percentage = (total_marks / 300) * 100
         
         return Response({'percentage':percentage}, status=200)
        return Response(serializer.errors) 
        