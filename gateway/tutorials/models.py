from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=255, blank=False, default='')
    lname = models.CharField(max_length=255, blank=False, default='')
    email = models.EmailField()

