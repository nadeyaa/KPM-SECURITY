from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('guard', 'Security Guard'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guard')

class Schedule(models.Model):
    date = models.DateField()
    shift = models.CharField(max_length=20)
    guard_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
