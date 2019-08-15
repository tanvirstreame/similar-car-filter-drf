'''
This file should serializers
'''
from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    '''
    VehicleSerializer
    '''
    class Meta:
        model = Vehicle
        fields = ('name', 'model', 'price', 'odometer_reading')
