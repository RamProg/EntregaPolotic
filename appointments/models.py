from django.db import models
from patient.models import Patient
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User, Group  

# Create your models here.

class Appointment(models.Model):

    appointmentChoices = (
        ('O','On hold'),
        ('A', 'Attended'),
        ('M', 'Missed'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    assistance = models.CharField(
        max_length=1, 
        choices=appointmentChoices,  
        verbose_name="assistance",
        blank=True,
        null=True,
        default = 'O'
    )
    medic = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, 
        blank=True,
        null=True
    )

    date = models.DateField(verbose_name="Date", default=timezone.now)

    def __str__(self):
        return f"{self.patient.name} {self.patient.lastName}, {self.date}"