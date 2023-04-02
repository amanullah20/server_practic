from django.db import models

# Create your models here.

class Students(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=38)
    student_email= models.CharField(max_length=30)
    batch = models.IntegerField()
    course = models.CharField(max_length=15)
