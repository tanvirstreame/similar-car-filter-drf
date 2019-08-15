from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.

class VehicleList(generics.ListCreateAPIView):
  serializer_class = VehicleSerializer
  queryset = Vehicle.objects.all()

class SimilerVehilceList(generics.ListCreateAPIView):
  serializer_class = VehicleSerializer
  # queryset = Vehicle.objects.all()
  queryset = Vehicle.objects.filter( price__lte=20000, odometer_reading__lte=200).order_by("price","odometer_reading")
  print(queryset)
