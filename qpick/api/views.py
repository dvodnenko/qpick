from django.http.request import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product, Headphone, Cover, Cart, CartItem, Order, OrderItem
from .serializers import HeadphoneSerializer, CoverSerializer, CartItemSerializer, OrderSerializer

# Create your views here.


class HeadphoneView(APIView):

    def get(self, request: HttpRequest):
        queryset = Headphone.objects.all()
        serializer = HeadphoneSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request: HttpRequest):
        serializer = HeadphoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CoverView(APIView):
    
    def get(self, request: HttpRequest):
        queryset = Cover.objects.all()
        serializer = CoverSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request: HttpRequest):
        serializer = CoverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AddToCartView(APIView):
    def post(self, request: HttpRequest):
        session_key = request.data.get('session_key')
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        product_id = request.data.get('product_id')
        product_type = request.data.get('product_type')
        quantity_to_add = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(
            session_key=session_key,
            defaults={
                'total_price': 0
            }
        )

        cart_item = CartItem.objects.filter(
            cart=cart,
            product=product,
            product_type=product_type,
        ).first()

        # user cannot have 3 products in the cart, if there are only 2 in the storage

        if not cart_item: # if created
            if quantity_to_add > product.quantity:
                return Response({'error': 'Quantity is Too Big'}, status=status.HTTP_403_FORBIDDEN)
            cart_item = CartItem(cart=cart, product=product, product_type=product_type, quantity=quantity_to_add)
        else: # if not created
            if cart_item.quantity + quantity_to_add > product.quantity:
                return Response({'error': 'quantity is Too big'}, status=status.HTTP_403_FORBIDDEN)
            cart_item.quantity += quantity_to_add

        cart_item.save()

        cart.total_price += (product.price * quantity_to_add)
        cart.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartView(APIView):
    def get(self, request: HttpRequest):
        session_key = request.GET.get('session_key')

        if not session_key:
            return Response({'error': 'Session Key is Required'}, status=status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.filter(session_key=session_key).first()
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderView(APIView):
    def get(self, request: HttpRequest):
        session_key = request.GET.get('session_key')

        if not session_key:
            return Response({'error': 'Session Key is Required'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.filter(session_key=session_key).first()
        order_items = CartItem.objects.filter(order=order)
        serializer = CartItemSerializer(order_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: HttpRequest):
        session_key = request.data.get('session_key')
        print(session_key)

        if not session_key:
            return Response({'error': 'Session Key is Required'}, status=status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.filter(session_key=session_key).first()

        if not cart or cart.total_price == 0: # then the cart is empty
            return Response({'error': 'Your Cart is Empty'}, status=status.HTTP_403_FORBIDDEN)

        cart_items = CartItem.objects.filter(cart=cart)

        order = Order(
            session_key=cart.session_key,
            total_price=cart.total_price
        )
        order.save()
        for ci in cart_items:
            order_item = OrderItem(
                order=order, 
                product=ci.product, 
                product_type=ci.product_type,
                quantity=ci.quantity
            )
            ci.product.quantity -= ci.quantity
            ci.product.save()
            order_item.save()
            if ci.product.quantity <= 0:
                ci.product.delete()
        
        # clean current user cart
        cart.delete()
        cart_items.delete()

        serializer = OrderSerializer(order, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
