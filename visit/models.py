from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class DoctorProfile(models.Model):
    choices = (
        ('Confirmation', 'Confirmation'),
        ('No Confirmation', 'No Confirmation')
    )
    fullname = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    expertise = models.CharField(max_length=500)
    status = models.CharField(max_length=16, choices=choices)

class PatientProfile(models.Model):
    fullname = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    national_code = models.CharField(max_length=10, blank=True)

class Visit(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.PROTECT)
    patient = models.ForeignKey(PatientProfile, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    
