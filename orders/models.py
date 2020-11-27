from django.db import models
from products.models import Product
from patient.models import Patient

# Create your models here.

class Order(models.Model):
    id = models.AutoField(primary_key= True)
    
    typePaymentChoices = [
    ('CC', 'Credit card'),
    ('DC', 'Debit card'),
    ('VW', 'Virtual wallet'),
    ('CS', 'Cash'),
    ]
    typePayment = models.CharField(
        max_length= 2,
        choices= typePaymentChoices,
        default='CS',
        )
    patient = models.ForeignKey(Patient ,blank=False, null=True, on_delete=models.CASCADE , related_name= "Order")
    sellDate = models.DateField(null = True)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Order nro. {self.id} - {self.patient}"