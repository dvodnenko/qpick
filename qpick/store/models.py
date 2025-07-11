from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=64, default='')
    price = models.IntegerField(default=1)
