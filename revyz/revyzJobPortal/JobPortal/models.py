from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)

    def __str__(self):
        return self.name


class Candidates(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )
    techskills = (
        ('Python', 'python'),
        ('Java', 'java'),
        ('Ruby', 'ruby'),
        ('Docker','docker'),
        ('Java Script', 'javascript'),
    )
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)    
    address = models.CharField(max_length= 500, null = True)
    city = models.CharField(max_length=200,null=True)
    techskill = models.CharField(max_length=200, null=True, choices=techskills)
    company=models.ManyToManyField(Company,blank=True)
    resume=models.FileField(null=True)
    
    def __str__(self):
        return self.name
