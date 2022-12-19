from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone


CATEGORY_CHOICES = [
    ('Education', 'Education'),
    ('Health', 'Health'),
    ('Governance', 'Governance'),
    ('Energy and Mining' , 'Energy and Mining')
]

class Project(models.Model):
    project_name= models.CharField(unique=True, max_length=1024)
    category= models.CharField(choices=CATEGORY_CHOICES , max_length=1024)
    affiliated_agency= models.CharField(max_length=1024)
    description= models.CharField( max_length=1024)
    project_start_time = models.DateField(default=timezone.now)
    project_completion_time= models.DateField(default=timezone.now)
    total_budget= models.CharField( max_length=64)
    def __str__(self):
        return self.project_name


class Location(models.Model):
    x_coor = models.FloatField()
    y_coor = models.FloatField()
    project = models.ForeignKey(Project , on_delete= models.CASCADE , related_name='Project')
    

