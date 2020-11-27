from django.db import models

# Create your models here.


class Patient(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    #orderPacient = models.OneToOneField(Order, blank= True,on_delete=models.CASCADE, related_name="Pacient")

    def __str__(self):
        return f"{self.name} {self.lastName}"