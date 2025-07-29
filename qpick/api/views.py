from django.http.request import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Product, Headphone, Cover, Cart, CartItem
from .serializers import HeadphoneSerializer, CoverSerializer, CartItemSerializer

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
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(
            session_key=session_key,
            defaults={
                'total_price': 0
            }
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            product_type=product_type,
            defaults={
                'quantity': quantity,
                'product_type': product_type,
            },
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartView(APIView):
    def get(self, request: HttpRequest):
        session_key = request.GET.get('session_key')

        if not session_key:
            return Response({'error': 'session_key is required'}, status=status.HTTP_400_BAD_REQUEST)

        cart = Cart.objects.filter(session_key=session_key).first()
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
