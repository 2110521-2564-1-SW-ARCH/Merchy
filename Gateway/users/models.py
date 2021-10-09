from django.db import models
import datetime
from django.forms.widgets import SelectDateWidget

# Create your models here.

# User = {
#     'fanme':    'foke',
#     'lname':    'nama',
#     'dob':      '01/01/1999',
#     'gender':   'M',
#     'email':    'foke@nama.com',
#     'password': 'abcdefgh',
#     'role':     'S',
# }


class User(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    # password = models.CharField(max_length=200)
    dob = models.DateField()
    # timestamp = models.DateTimeField(auto_now_add=True)

    GENDER_CHOICES = [
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Others',), 
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

    ROLE_CHOICES = [
        ('S', 'Seller',),
        ('B', 'Buyer',),
    ]
    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES
    )


    def __str__(self):
        return f'{self.fname} {self.lname} {self.email} {self.dob} {self.gender} {self.role}'

