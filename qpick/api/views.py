from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from store.models import Headphone, Cover
from .serializers import HeadphoneSerializer, CoverSerializer

# Create your views here.


class HeadphoneView(APIView):

    def get(self, request):
        queryset = Headphone.objects.all()
        serializer = HeadphoneSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HeadphoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CoverView(APIView):
    
    def get(self, request):
        queryset = Cover.objects.all()
        serializer = CoverSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CoverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
