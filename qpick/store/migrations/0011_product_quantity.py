# Generated by Django 5.2.4 on 2025-07-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_cart_remove_cartitem_session_key_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
