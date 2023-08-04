from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    worldmap = models.CharField(max_length=80)
    
    