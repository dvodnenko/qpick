from django.contrib import admin

from .models import Headphone, Cover, CartItem, Order

# Register your models here.


@admin.register(Headphone, Cover, CartItem, Order)
class Store(admin.ModelAdmin):
    ...
