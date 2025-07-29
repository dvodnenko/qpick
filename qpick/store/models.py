from django.db import models

from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.


class Product(models.Model):
    currency_choices = [
        ('₴', 'uah'),
        ('$', 'usd')
    ]

    title = models.CharField(max_length=64, default='')
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(default=1)
    currency = models.CharField(choices=currency_choices, default='₴')
    image = models.ImageField(default='/static/default-image.webp', upload_to='products/', storage=MediaCloudinaryStorage)


class Headphone(Product):
    ...

class Cover(Product):
    ...

class Cart(models.Model):
    session_key = models.CharField(max_length=40, blank=True)
    total_price = models.IntegerField(default=0)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=16, default='')
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.title} x{self.quantity} [{self.cart.session_key}]'
