from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=40)
    emp_email=models.EmailField()
    emp_Joining=models.DateField()
    emp_dep=models.CharField(max_length=40)
    emp_contact=models.IntegerField()
    emp_age=models.IntegerField()
    emp_image=models.ImageField(upload_to='image/',null=True,blank=True,max_length=200)
    emp_password=models.IntegerField()

