# Generated by Django 5.2.4 on 2025-08-01 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
    ]
