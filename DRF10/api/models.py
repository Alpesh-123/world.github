from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    maths_marks = models.DecimalField(max_digits=5, decimal_places=2)
    physics_marks = models.DecimalField(max_digits=5, decimal_places=2)
    chemistry_marks = models.DecimalField(max_digits=5, decimal_places=2)
   
    def __str__(self):
        return self.name