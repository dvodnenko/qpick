from django.db import models

from cloudinary_storage.storage import MediaCloudinaryStorage

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=64, default='')
    price = models.IntegerField(default=1)
    image = models.ImageField(default='/static/default-image.webp', upload_to='products/', storage=MediaCloudinaryStorage)


class Headphone(Product):
    ...

class Cover(Product):
    ...
