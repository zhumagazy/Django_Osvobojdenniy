from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    info=models.TextField()
    price=models.IntegerField()
    type=models.CharField(max_length=30)