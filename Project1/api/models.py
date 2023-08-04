from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    maths_marks = models.DecimalField(max_digits=5, decimal_places=2 )
    science_marks = models.DecimalField(max_digits=5, decimal_places=2 )
    history_marks = models.DecimalField(max_digits=5, decimal_places=2 )
    
    def __str__(self):
        return self.name


