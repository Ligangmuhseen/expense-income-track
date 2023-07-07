from django.db import models

# Create your models here.

class Transaction(models.Model):
    text = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

