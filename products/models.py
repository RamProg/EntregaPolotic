from django.db import models

# Create your models here.

class Lens(models.Model):

    name = models.CharField(max_length=60)
    includeFrame = models.BooleanField()

    

    Side = (
        ('L', 'Left'),
        ('R', 'Right'),
        ('B', 'Both'),
    )
    
    side = models.CharField(max_length=1, choices=Side)
        

    Magnification = (
        ('F', 'Far'),
        ('C', 'Close'),
        
    )
    
    magnification = models.CharField(max_length=1, choices=Magnification)

    def __str__(self):
        return f" {self.name} - frame:{self.includeFrame} - {self.side} - {self.magnification}"


class Product(models.Model):
    name = models.CharField(max_length=50)
    lens = models.ForeignKey(Lens, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f" {self.name} - Price: ${self.price}"