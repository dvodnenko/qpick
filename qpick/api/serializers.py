from rest_framework import serializers
from store.models import Product, Headphone, Cover, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'currency', 'image']


class HeadphoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headphone
        fields = ['id', 'title', 'price', 'currency', 'image']


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = ['id', 'title', 'price', 'currency', 'image']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['session_key', 'total_price']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'product_type']
