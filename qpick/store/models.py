from django.db import models
from django.contrib.auth.models import User

from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.


class Product(models.Model):
    currency_choices = [
        ('₴', 'uah'),
        ('$', 'usd')
    ]

    title = models.CharField(max_length=64, default='')
    price = models.IntegerField(default=1)
    currency = models.CharField(choices=currency_choices, default='₴')
    image = models.ImageField(default='/static/default-image.webp', upload_to='products/', storage=MediaCloudinaryStorage)


class Headphone(Product):
    ...

class Cover(Product):
    ...

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

