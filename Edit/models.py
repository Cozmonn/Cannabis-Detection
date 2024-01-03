from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    BadgeID = models.CharField(max_length=30, unique=True, primary_key=True)
    CNI = models.CharField(max_length=30, unique=True)
    Image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default=None)
    first_name = models.CharField(max_length=30, default=None)
    last_name = models.CharField(max_length=30, default=None)
    fonction = models.CharField(max_length=30, default=None)
    BirthdayDay = models.DateField(max_length=30, default=None)
    Zone = models.CharField(max_length=30, default=None)
    Permission = models.CharField(max_length=30, default=None)
    account = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)