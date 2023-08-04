from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'maths', 'physics', 'chemistry', 'total_marks', 'percentage']
        