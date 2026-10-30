from django.db import models

# Create your models here.
class Fooditem(models.Model):
    food_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits =6, decimal_places =2)
    quantity = models.IntegerField()
