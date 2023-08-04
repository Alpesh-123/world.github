from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    geography = models.IntegerField()
    astrology = models.IntegerField()