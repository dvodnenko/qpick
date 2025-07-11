from django.contrib import admin

from .models import Headphone, Cover

# Register your models here.


@admin.register(Headphone, Cover)
class Store(admin.ModelAdmin):
    ...
