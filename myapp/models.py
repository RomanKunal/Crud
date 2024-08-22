from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    dob = models.DateField()
    department = models.CharField(max_length=100)  

    def __str__(self):
        return self.name
