from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Module(models.Model):

    name = models.CharField(max_length=100)

  

class Profile (models.Model):

    GENDER = {
        ('M', 'Male'),
        ('F', 'Female')
    }
        

    
 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    gender = models.CharField(max_length=1, choices=GENDER,default=None)
    dateOfBirth = models.DateField('Date of Birth')
    modules = models.ManyToManyField(Module)

    def getAge(self):
        today = date.today()

        return today.year - self.dateOfBirth.year - ((today.month, today.day) < (self.dateOfBirth.month, self.dateOfBirth.day))

 




