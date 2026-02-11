from django.db import models

class KeyMetrics(models.Model):
    category=models.CharField(max_length=200)
    price=models.FloatField()
    sale=models.FloatField()


    def __str__(self):
     return f"{self.category} - Price: {self.price} - Sale: {self.sale}"
