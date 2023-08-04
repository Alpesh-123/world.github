from django.shortcuts import render
from rest_framework.views  import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import action

class CalculatePercentage(APIView):
    def post(self, request):
     serializer = StudentSerializer(data=request.data)
     if serializer.is_valid():
        maths = request.data.get("maths")
        physics = request.data.get("physics")
        chemistry = request.data.get("chemistry")
        geography = request.data.get("geography")
        astrology = request.data.get("astrology")
        
        total_marks = maths + physics + chemistry + geography + astrology
        
        percentage =  (total_marks / 500) * 100
        
        
        return Response({'percentage': percentage})

        
        
        