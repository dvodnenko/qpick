from django.contrib import admin

from .models import Headphone, Cover, CartItem

# Register your models here.


@admin.register(Headphone, Cover, CartItem)
class Store(admin.ModelAdmin):
    ...
