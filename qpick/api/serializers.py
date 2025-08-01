from rest_framework import serializers
from store.models import Product, Headphone, Cover, Cart, CartItem, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image', 'quantity']


class HeadphoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Headphone
        fields = ['id', 'title', 'price', 'image', 'quantity']


class CoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cover
        fields = ['id', 'title', 'price', 'image', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['session_key', 'total_price']


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'product_type']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['session_key', 'total_price']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'product_type']
