from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from project.models import Project
from users.models import User


class Issue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    issue = models.CharField(max_length=1024)
    def __str__(self):
        return f'{self.user} on {self.project}: {self.issue}' 
