from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class CalculatePercentage(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            maths_marks = serializer.validated_data['maths_marks']
            science_marks = serializer.validated_data['science_marks']
            history_marks = serializer.validated_data['history_marks']
            
            total_marks = maths_marks + science_marks + history_marks
            print(total_marks)
            percentage = (total_marks / 300) * 100
            print(percentage)
            
            return Response({'percentage': percentage})
        return Response(serializer.errors) 