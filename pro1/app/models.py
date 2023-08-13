from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Place(models.Model):
    image =models.FileField(upload_to='images/img',null=True,blank=True)
    name =models.CharField(max_length=20)
    desc= models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    img=models.FileField(upload_to='team/img',null=True,blank=True)
    name=models.CharField(max_length=20)
    desc= models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class MyUser(AbstractUser):
    place = models.CharField(max_length=20)
    number = models.CharField(max_length=20)

    
    


