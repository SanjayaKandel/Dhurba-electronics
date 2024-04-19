from django.db import models

# Create your models here.
class Items(models.Model):
    image = models.ImageField(upload_to='static/image/', null=True, blank=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Accessories(models.Model):
    image = models.ImageField(upload_to='static/image/', null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
