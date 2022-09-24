from django.db import models

# Create your models here.
class student_details(models.Model):
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    curadd=models.CharField(max_length=150)
    email=models.CharField(max_length=100)
    paswd=models.CharField(max_length=100)

    def __str__(self):
        return self.fname+" "+self.course
        