from rest_framework import viewsets 
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class CalculatePercentageViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def calculate_percentage(self, request):
        maths = request.data.get('maths')
        physics = request.data.get('physics')
        chemistry = request.data.get('chemistry')
        
        total_marks = maths + physics + chemistry
        
        percentage = (total_marks / 300) * 100
        
        return Response({'percentage':percentage}, status=200)
        