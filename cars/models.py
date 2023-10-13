from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20, unique=True)
    milage = models.IntegerField()
    model = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return f'Make : {self.make} | Reg No : {self.reg_no}'
   
