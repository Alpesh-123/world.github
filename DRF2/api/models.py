from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    maths = models.DecimalField(max_digits=5, decimal_places=2)
    physics = models.DecimalField(max_digits=5, decimal_places=2)
    chemistry = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=3)
    percentage = models.FloatField()
    
   