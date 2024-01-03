from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    Fullname = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
