from django.db import models
from django.contrib.auth.models import User

class BioData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)


class detailspage(models.Model):
    details_id=models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name