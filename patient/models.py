from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    age = models.PositiveIntegerField(default = 0, null = False)
    dni = models.CharField(max_length=11, unique=True, default= "0")
    #orderPacient = models.OneToOneField(Order, blank= True,on_delete=models.CASCADE, related_name="Pacient")
    email = models.EmailField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.name} {self.lastName}"