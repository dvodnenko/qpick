from django.shortcuts import render
from rest_framework import viewsets

from store.models import Headphone, Cover
from .serializers import HeadphoneSerializer, CoverSerializer

# Create your views here.


class HeadphoneView(viewsets.ModelViewSet):
    queryset = Headphone.objects.all()
    serializer_class = HeadphoneSerializer


class CoverView(viewsets.ModelViewSet):
    queryset = Cover.objects.all()
    serializer_class = CoverSerializer
